import json
import streamlit as st
import os
from typing import Tuple, Optional
from groq import Groq

st.set_page_config(layout="wide")

FILEPATH = "agents.json"
MODEL_MAX_TOKENS = {
    'mixtral-8x7b-32768': 32768,
    'llama2-70b-4096': 4096,
    'gemma-7b-it': 8192,
}

def load_agent_options() -> list:
    agent_options = ['Create an expert...']
    if os.path.exists(FILEPATH):
        with open(FILEPATH, 'r') as file:
            try:
                agents = json.load(file)
                agent_options.extend([agent["agent"] for agent in agents if "agent" in agent])
            except json.JSONDecodeError:
                st.error("Error reading the agents file. Please check its format.")
    return agent_options

def get_max_tokens(model_name: str) -> int:
    return MODEL_MAX_TOKENS.get(model_name, 4096)

def refresh_page():
    st.experimental_rerun()

def save_expert(expert_title: str, expert_description: str):
    with open(FILEPATH, 'r+') as file:
        agents = json.load(file) if os.path.getsize(FILEPATH) > 0 else []
        agents.append({"agent": expert_title, "description": expert_description})
        file.seek(0)
        json.dump(agents, file, indent=4)
        file.truncate()

def fetch_assistant_response(user_input: str, model_name: str, temperature: float, agent_selection: str) -> Tuple[str, str]:
    phase_two_response = ""
    expert_title = ""

    try:
        groq_api_key = os.environ.get("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("GROQ_API_KEY environment variable not set.")

        client = Groq(api_key=groq_api_key)

        def get_completion(prompt: str) -> str:
            completion = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                model=model_name,
                temperature=temperature,
                max_tokens=get_max_tokens(model_name),
                top_p=1,
                stop=None,
                stream=False
            )
            return completion.choices[0].message.content

        if agent_selection == "Create an expert...":
            phase_one_prompt = f"Act as an expert prompt engineer. Analyze the following input to determine the title and characteristics of the best expert to answer the question. Begin the response with the expert's title followed by a period ['.'], then provide a concise description of that expert: {user_input}"
            phase_one_response = get_completion(phase_one_prompt)
            first_period_index = phase_one_response.find(".")
            expert_title = phase_one_response[:first_period_index].strip()
            expert_description = phase_one_response[first_period_index + 1:].strip()
            save_expert(expert_title, expert_description)
        else:
            with open(FILEPATH, 'r') as file:
                agents = json.load(file)
                agent_found = next((agent for agent in agents if agent["agent"] == agent_selection), None)
                if agent_found:
                    expert_title = agent_found["agent"]
                    expert_description = agent_found["description"]
                else:
                    raise ValueError("Selected expert not found in the file.")

        phase_two_prompt = f"Act as {expert_title}, an expert on the topic, and provide a thorough and well-formatted response to the following question: {user_input}"
        phase_two_response = get_completion(phase_two_prompt)

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "", ""

    return expert_title, phase_two_response

agent_options = load_agent_options()

st.title("Groqbot Experts")
st.write("Enter your request to have it addressed by the ideal expert.")

col1, col2 = st.columns(2)

with col1:
    user_input = st.text_area("Please enter your request:", "", key="user_input")
    agent_selection = st.selectbox("Choose an Expert", options=agent_options, index=0, key="agent_selection")
    model_name = st.selectbox("Choose a Model", list(MODEL_MAX_TOKENS.keys()), index=0, key="model_name")
    temperature = st.slider("Creativity Level", min_value=0.0, max_value=1.0, value=0.0, step=0.01, key="temperature")
    max_tokens = get_max_tokens(model_name)
    st.write(f"Max Tokens for selected model: {max_tokens}")

    if st.button("Fetch Response"):
        ideal_expert_description, assistant_response = fetch_assistant_response(user_input, model_name, temperature, agent_selection)
        col2.write(f"**Expert Analysis:**\n{ideal_expert_description}\n\n**Expert's Response:**\n{assistant_response}")

    if st.button("Refresh"):
        refresh_page()