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
        {"role": "system", "content": "You are a named entity recognition assistant. Extract all person names, organization names, Languages and locations from the user's text, and return them in JSON format with keys 'persons', 'organizations','languages', 'locations'."},
        {"role": "user", "content": "I am D Sameer Kumar Reddy, from Andhra Pradesh I work for SRH as performance analyst. I bleed for telugu teams. I love cricket and kabaddi. "}
    ]
)

print(response.choices[0].message.content)

