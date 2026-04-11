from openai import OpenAI
client = OpenAI(
  api_key=""
)

response = client.responses.create(
    model="gpt-5-nano",
    input="hello, who are you"
)

print(response.output_text)