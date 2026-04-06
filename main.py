"""Run this model in Python

> pip install azure-ai-inference
"""
import os
from dotenv import load_dotenv

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

load_dotenv()  # This loads the variables from .env

# To authenticate with the model you will need to generate a personal access token (PAT) in your GitHub settings. 
# Create your PAT token by following instructions here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens
client = ChatCompletionsClient(
    endpoint="https://models.github.ai/inference",
    credential=AzureKeyCredential(os.getenv("GITHUB_TOKEN")),
)

response = client.complete(
    messages=[
        SystemMessage("""You are a helpful assistant."""),
        UserMessage("Tell me the basics of cybernetics"),
    ],
    model="meta/Llama-3.3-70B-Instruct",
    temperature=1.0,
    max_tokens=1000,
    top_p=1.0
)

print(response.choices[0].message.content)
