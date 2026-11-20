from openai import AzureOpenAI
endpoint = "https://srh-1.services.ai.azure.com/"
api_key = ""
deployment_name = "gpt-5-mini"

# 4. Use AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-12-01-preview"  # Use a recent stable API version
)

# 5. Call the model (model parameter uses deployment name)
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a key phrase extraction Ai. Extract 3-5 important key phrases from user provided content "}
        {"role": "user", "content": "Abhishek is the fastest to scor 200 runs in balls "}
    ]
)

print(response.choices[0].message.content)