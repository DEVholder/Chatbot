import openai
import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI API 인증
openai.api_key = os.environ.get('OPENAI_API_KEY')

# ChatGPT 초기화
chatgpt = openai.Completion.create(engine="davinci", prompt="Hello, world!", max_tokens=10)

# 대화하기
prompt = "Hi?"
chatgpt = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=10)
message = chatgpt.choices[0].text.strip()
print(message)
