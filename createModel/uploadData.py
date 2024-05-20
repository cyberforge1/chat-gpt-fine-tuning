# Uploads the Data to the API for processing
import os
from dotenv import load_dotenv
import openai

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
print(f'API Key: {api_key}')

openai.api_key = api_key

response = openai.File.create(
    file=open("formattedData.jsonl", "rb"),
    purpose="fine-tune"
)

print(response)
