# ChatGPT Fine Tuning

## Project Overview
This project includes a series of Python scripts designed to generate data and train a finely-tuned ChatGPT model.


## Useful Commands:

### Create venv

- python -m venv venv

### Activate venv

- source venv/bin/activate

### Downloading Dependencies

- pip freeze > requirements.txt


## How to Use:

## Part 1: Data Generation & Training

1) Create an xlsx file with a list of prompts for ChatGPT or use the provided ./data/promptData.xlsx file
2) Run generateData.py to create responses to each one of these prompts dynamically
3) Specifying the type of data to be generated can be achieved in the chat_with_gpt3 function in generateData.py 
3) Run formatConverter.py to generate a .jsonl file, which prepares and formats the data for upload
4) Run uploadData.py to upload the data to the OpenAI API for processing
5) Run createModel.py to start fine-tuning the ChatGPT model
6) Check the progress with checkModel.py

## Part 2: Accessing the Model

1) The createModel.py script will return a model number for your specific finely tuned model or your can access this through the OpenAI Fine Tuning web portal (https://platform.openai.com/docs/guides/fine-tuning).
2) The callsToModel.py script can make specific calls to your newly created finely-tuned model.

- This can be achieved by replacing "ft:gpt-3.5-turbo-0125:personal::XXXXXXXX" with your specific model ID
& "Here is a test prompt" with a specific prompt



