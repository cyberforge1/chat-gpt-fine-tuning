import openpyxl
import requests
import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print(api_key)

# Set the API key for OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt3(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using the GPT-3.5 Turbo model
            messages=[
                {"role": "user", "content": prompt + " with the response being provided in poetry, as a limerick"}
            ],
            max_tokens=150  # Adjust this value to control the response length
        )
        print(response['choices'][0]['message']['content'].strip())
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return str(e)
    
completion = chat_with_gpt3('testing')
print(completion)