from openai import OpenAI
import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

print("API Key:", openai.api_key)


def generate_completion(prompt):
    
    client = OpenAI()

    completion = client.chat.completions.create(
        model="ft:gpt-3.5-turbo-0125:personal::XXXXXXXX",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    return completion.choices[0].message

prompt = "Here is a test prompt!"
response = generate_completion(prompt)
print(response)