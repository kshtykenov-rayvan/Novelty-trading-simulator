import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("API key not found. Please check your .env file and environment setup.")

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "user", 
         "content": "Say hello!"}
    ]
)

print(response.choices[0].message['content'])
