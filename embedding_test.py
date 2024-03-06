from openai import OpenAI

client = OpenAI()

result = client.embeddings.create(model="text-embedding-ada-002", input="Hello world",encoding_format="float")
print(result.data[0].embedding)
