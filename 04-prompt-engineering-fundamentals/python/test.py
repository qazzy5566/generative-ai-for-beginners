import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# This test is working

success = load_dotenv()

endpoint = os.environ['AZURE_OPENAI_ENDPOINT']
model_name = "gpt-4o-mini"
deployment = os.environ['AZURE_OPENAI_DEPLOYMENT']
subscription_key = os.environ['AZURE_OPENAI_API_KEY']
api_version = os.environ['AZURE_OPENAI_API_VERSION']

print( endpoint )
print( api_version )

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)

print(response.choices[0].message.content)