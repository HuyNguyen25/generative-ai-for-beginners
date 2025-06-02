from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv() #loading environment variables
client = AzureOpenAI(
    api_key = os.environ['AZURE_OPENAI_API_KEY'],
    azure_endpoint = os.environ['AZURE_OPENAI_ENDPOINT'],
    api_version = os.environ['AZURE_OPENAI_API_VERSION']
)

deployment = os.environ['AZURE_OPENAI_DEPLOYMENT']

prompt = "Who plays Jack Sparrow?"
messages = [
    {
        "role": "user",
        "content": prompt
    }
]

completion = client.chat.completions.create(
    model = deployment,
    messages = messages
)

print(completion.choices[0].message.content)