import pandas as pd
import json

# Load the dataset from the Excel file
data_path = "../data/promptData.xlsx"
formatted_data_path = "formattedData.jsonl"

def convert_data_format(original_file, new_file):
    # Read the Excel file
    df = pd.read_excel(original_file, usecols=['prompt', 'completion'])
    
    with open(new_file, 'w', encoding='utf-8') as nf:
        for index, row in df.iterrows():
            # Create a system prompt
            system_prompt = {
                "role": "system",
                "content": "You are an assistant."
            }
            # User prompt based on the 'prompt' column
            user_prompt = {
                "role": "user",
                "content": row['prompt']
            }
            # Assistant's response based on the 'completion' column
            assistant_response = {
                "role": "assistant",
                "content": row['completion']
            }
            # Compile into a new format
            formatted_example = {"messages": [system_prompt, user_prompt, assistant_response]}
            # Write the new format to a new file
            nf.write(json.dumps(formatted_example) + "\n")

# Call the function to convert data
convert_data_format(data_path, formatted_data_path)