from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    raise ValueError("API key is not set. Please check your .env file.")

client = OpenAI(api_key=api_key)

try:
    job = client.fine_tuning.jobs.create(
        training_file="file-aW0V63GFJPDuhx0kfQTJ9Yhh",
        model="gpt-3.5-turbo"
    )
    print("Job created successfully:", job.id)
except Exception as e:
    print("Failed to create job:", e)