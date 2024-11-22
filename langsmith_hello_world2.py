# pip install -U langchain langchain-openai
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from openai import AzureOpenAI
from langsmith.wrappers import wrap_openai
from langsmith import traceable

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    azure_deployment=os.getenv("MODEL_NAME"),
    )

@traceable # Auto-trace this function
def pipeline(user_input: str):
    result = client.chat.completions.create(
        messages=[{"role": "user", "content": user_input}],
        model="gpt-4o-mini"
    )
    return result.choices[0].message.content

pipeline("Hello, world!")
# Out:  Hello there! How can I assist you today?