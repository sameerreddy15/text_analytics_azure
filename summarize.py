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
long_text="""Sunrisers Hyderabad entered the IPL with a dream of becoming the strongest team in cricket.Led by their captain, the players worked hard and fought together in every match.
With powerful batting, brilliant bowling, and amazing teamwork, they won the hearts of millions of fans.The Orange Army cheered loudly, supporting their team through every victory and defeatTogether, Sunrisers Hyderabad continued their journey with one dream: Rise Up, Orange Army!"""
# 5. Call the model (model parameter uses deployment name)
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a Text summarization assistant. Summarize the user's content into one consise sentiment."},
        {"role": "user", "content": long_text}
    ]
)

print(response.choices[0].message.content)

