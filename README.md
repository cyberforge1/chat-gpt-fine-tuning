# ChatGPT Fine-Tuning Python Scripts


## Project Overview
This project includes a series of Python scripts designed to generate training data and create a finely-tuned ChatGPT model. Find the training guide below: 

[https://platform.openai.com/docs/guides/fine-tuning](https://platform.openai.com/docs/guides/fine-tuning)

## Table of Contents
- [Tech Stack](#tech-stack)
- [Build Steps](#build-steps)
- [Design Goals](#design-goals)
- [Project Features](#project-features)
- [Additions & Improvements](#additions--improvements)
- [Learning Highlights](#learning-highlights)

## Tech Stack
- Python
- ChatGPT 3.5 Turbo API

## Build Steps

### Project Set-up
1. Clone the project from GitHub:
   ```bash
   git clone git@github.com:cyberforge1/chat-gpt-fine-tuning.git

2. Register for an OpenAI API key at the following link.

   [https://openai.com/index/openai-api/](https://openai.com/index/openai-api/)

3. Create a `.env` file in the root directory and attach the values of the key obtained in step 2.

    ```plaintext
    OPENAI_API_KEY= replace_with_your_openai_api_key
    ```

4. Create a new virtual environment 
   ```bash
   python -m venv venv

4. Create a new virtual environment 
   ```bash
   python -m venv venv

5. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```

6. Install project dependencies with pip:
    ```bash
    pip install -r requirements.txt
    ```

## How to Use:

### Part 1: Data Generation & Training

1) Create an xlsx file with a list of prompts for ChatGPT or use the provided ./data/promptData.xlsx file
2) Run generateData.py to create responses to each one of these prompts dynamically
3) Specifying the type of data to be generated can be achieved in the chat_with_gpt3 function in generateData.py 
4) Run formatConverter.py to generate a .jsonl file, which prepares and formats the data for upload
5) Run uploadData.py to upload the data to the OpenAI API for processing
6) Run createModel.py to start fine-tuning the ChatGPT model
7) Check the progress with checkModel.py

### Part 2: Accessing the Model

1) The createModel.py script will return a model number for your specific finely tuned model or your can access this through the OpenAI Fine Tuning web portal (https://platform.openai.com/docs/guides/fine-tuning).
2) The callsToModel.py script can make specific calls to your newly created finely-tuned model.

- This can be achieved by replacing "ft:gpt-3.5-turbo-0125:personal::XXXXXXXX" with your specific model ID
& "Here is a test prompt" with a specific prompt

## Project Features
- [x] A base dataset containing 200 queries
- [x] Scripts that automate the creation of specific training data
- [x] Scripts that transfer the data into desired format and train a finely-tuned ChatGPT model

## Additions & Improvements
- [ ] Refactoring scripts for efficiency 
- [ ] Chaining scripts together for more simple execution


## Learning Highlights
- Strengthened skills with Python scripting and automation
- Experience training a chatbot model with custom data


## Contact Me
- Visit my [LinkedIn](https://www.linkedin.com/in/obj809/) for more details.
- Check out my [GitHub](https://github.com/cyberforge1) for more projects.
- Or send me an email at obj809@gmail.com
<br />
Thanks for your interest in this project. Feel free to reach out with any thoughts or questions.
<br />
<br />
Oliver Jenkins © 2024
