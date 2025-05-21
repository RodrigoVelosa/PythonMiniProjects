import requests
import sys
import re

BASE_URL = 'http://127.0.0.1:1234/'

HEALTH_METRICS_CSV_FILE_PATH = 'HealthMetrics.csv'

def post_chat_completions():
    question = input("Entao?\n")
    deepseek_question(question)

def deepseek_question(questions):
    endpoint = BASE_URL + 'v1/chat/completions'

    messages = []

    if isinstance(questions, str):
        questions = [questions]

    for question in questions:
        messages.append({"role": "user", "content": question})

    payload = {
        "model": "deepseek-r1-distill-qwen-7b",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": -1,
        "stream": False
    }

    response = requests.post(endpoint, json=payload)

    if response.status_code != 200:
        print("Fail :(")
        sys.exit()
    
    generated_response = response.json()
    answer = generated_response.get("choices")[0].get("message").get("content")
    filtered_answer = re.sub(r"<think>.*</think>", "", answer, flags=re.DOTALL).strip()

    print(filtered_answer)

def get_models():
    endpoint = BASE_URL + 'v1/models'
    response = requests.get(endpoint)

    if response.status_code != 200:
        print("Fail :(")
        sys.exit()

    generated_response = response.json()
    print(generated_response)

def health_metrics():
    try:
        with open(HEALTH_METRICS_CSV_FILE_PATH, 'r') as file:
            csv_content = file.read()
    except FileNotFoundError:
        print('Error: Missing File')

    question = f"Analyze the below health data: {csv_content}. Please give me a health report and suggest improvements"
    deepseek_question(question)

def chatbot():
    allquestions = []
    while True:
        currQuestion = input("").strip()

        if currQuestion.lower() in ['exit', 'quit']:
            break

        allquestions.append(currQuestion)
        deepseek_question(allquestions)

chatbot()