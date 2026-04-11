from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="omni-moderation-latest",
    input="hello, who are you"
)

print(response.output_text)