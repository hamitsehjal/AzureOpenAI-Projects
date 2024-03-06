''' Azure OpenAI Project - Tweet Generator '''

import os
from typing import List
from dotenv import load_dotenv
# load environmental variables
load_dotenv()

from openai import AzureOpenAI

# Configure AzureOpenAI Client 
client=AzureOpenAI(
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
api_key = os.getenv("AZURE_OPENAI_API_KEY"),
api_version = os.getenv("AZURE_API_VERSION"),
)

def askGPT(client,messages):
    '''make request to OpenAI GPT model using client and messages'''
    response=client.chat.completions.create(model="gpt-35",messages=messages)
    return response.choices[0].message.content

system_prompt="You are a tweet generator. \
Your task is to generate tweets, based on the TOPICS and HASTAGS that are given to you. \
You should respect the instructions: the TONE, the LENGTH, and the STYLE"

def generate_tweet(topics: List[str], hastags: List[str], tone: str, length_characters: int, style: str):
    '''Generate tweet based on the parameters'''
    topics=",".join(topics)
    hastags=",".join(['#' + tag for tag in hastags])
    user_prompt=f"\
        TOPICS: {topics} \
        HASTAGS: {hastags} \
        TONE: {tone} \
        LENGTH: {length_characters} characters \
        STYLE: {style}"
    
    return askGPT(client,[{"role":"system","content":system_prompt},{"role":"user","content":user_prompt}])
    
     
