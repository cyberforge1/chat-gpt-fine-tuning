from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if api_key is None:
    raise ValueError("API key is not set. Please check your .env file.")

client = OpenAI(api_key=api_key)


# Retrieve the state of a fine-tune
state_response = client.fine_tuning.jobs.retrieve("ftjob-jzt8OpmH2OSnUrndQBqHy2BS")
print("State response:", state_response)

# List up to 10 events from a fine-tuning job
# events_response = client.fine_tuning.jobs.list_events(fine_tuning_job_id="ftjob-jzt8OpmH2OSnUrndQBqHyXXX", limit=10)
# print("Events response:", events_response)

# List 10 fine-tuning jobs
# client.fine_tuning.jobs.list(limit=10)

# Cancel a job
# client.fine_tuning.jobs.cancel("ftjob-abc123")

# Delete a fine-tuned model (must be an owner of the org the model was created in)
#client.models.delete("ft:gpt-3.5-turbo:acemeco:suffix:abc123")