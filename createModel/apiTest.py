import openpyxl
import requests
import os
import openai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print(api_key)

openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_gpt3(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt + " with the response being provided in poetry, as a limerick"}
            ],
            max_tokens=150
        )
        print(response['choices'][0]['message']['content'].strip())
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return str(e)
    
completion = chat_with_gpt3('testing')
print(completion)