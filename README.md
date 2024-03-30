## Groqbot has evolved into AutoGroq:  https://www.youtube.com/watch?v=CzMdqZ83eBk 

# Groqbot Experts

## Introduction

Groqbot Experts is an innovative Streamlit application designed to create and save specialized expert agents for addressing their unique inquiries. 

Leveraging the power of AI through various language models via the speed of Groq, this application dynamically selects or creates the most suitable expert to provide detailed and insightful responses to user questions.

Free online demo:  https://groqbot-expertsgit-mkg25rn7dyak86drvdztnq.streamlit.app/  

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Documentation](#documentation)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Contributors](#contributors)
- [License](#license)

## Features

- Dynamic expert creation based on user input.
- Integration with multiple language models.
- Customizable interaction parameters (model selection, temperature).
- Streamlit-based UI for easy and interactive use.

## Installation

To set up the Groqbot Experts application, follow these steps:

1. Clone the repository:
   ```git clone <repository-url>```

2. Navigate to the cloned repository directory:
```cd groqbot-experts```

3. Install the required Python packages:
```pip install -r requirements.txt```


## Usage

To run Groqbot Experts, execute the following command in your terminal:

```streamlit run app.py```


After starting the application, navigate to the displayed URL in your web browser to interact with Groqbot Experts.

## Dependencies

- Python 3.x
- Streamlit
- os
- json

Ensure you have Python installed on your system and use `pip` to install Streamlit along with any other dependencies.

## Configuration

Before using the application, set the `GROQ_API_KEY` environment variable to your Groq API key:

```export GROQ_API_KEY='your_api_key_here'```


## Documentation

For more detailed information on the Groq API and Streamlit framework, refer to the following resources:

- [Groq API Documentation](https://docs.groq.com/api)
- [Streamlit Documentation](https://docs.streamlit.io/)

## Examples

Here is an example of how to interact with Groqbot Experts:

1. Enter a detailed inquiry in the text area provided.
2. Select an existing expert from the dropdown or choose to create a new one.
3. Choose a language model and set the creativity level.
4. Click on "Fetch Response" to view the expert's analysis and response.

## Troubleshooting

If you encounter issues with missing environment variables or JSON file errors, ensure your `GROQ_API_KEY` is correctly set and the `agents.json` file is properly formatted and accessible.

## Contributors

To contribute to Groqbot Experts, please fork the repository, make your changes, and submit a pull request for review.

## License

Groqbot Experts is released under the MIT License. See the LICENSE file in the repository for more details.


