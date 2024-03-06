'''
Hello world completion Test Project with OpenAI
'''
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(model="gpt-3.5-turbo",messages=[
{"role":"system", "content":"You are a programmer turned University Teacher"},
{"role":"user", "content":"Hello World"},
{
"role":"assistant",
"content":"Yo, you can't say that in class",
},
{
"role":"user",
"content":"So, what can we say",
},
])

# extract the response
print(response.choices[0].message.content)
