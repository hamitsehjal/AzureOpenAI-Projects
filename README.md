# Building LLMs powered Apps using Azure OpenAI 

### Video Summarizer 
- Built using `Azure OpenAI GPT-35-Turbo`
- Deployed using `Gradio`

### Tweet Generator
- Built using `Azure OpenAI GPT-35-Turbo`
- Deployed using `Gradio`

## Prerequisites

1. 
Run the following commands to install the Dependencies


## Setup

1. Clone the Repository
```python
git clone https://github.com/hamitsehjal/AzureOpenAI-Projects
```

2. Install Dependencies
```
pip install -r requirements.txt
```
3. Configure Azure OpenAI Credentials - an `.env` file in the root of the project with following Environment Variables
```
AZURE_OPENAI_ENDPOINT=
AZURE_OPENAI_API_KEY=
AZURE_DEPLOYMENT_NAME=
AZURE_API_VERSION=
```
4. Run the Scripts
```python
python tweet_generator.py
```
```python
python video_summarizer.py
```

## Demo

### Tweet Generator

### Video Summarizer