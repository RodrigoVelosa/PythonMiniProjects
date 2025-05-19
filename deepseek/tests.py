import requests
import sys

BASE_URL = 'http://127.0.0.1:1234/'

def post_chat_completions():
    endpoint = BASE_URL + 'v1/chat/completions'

    payload = {
        "model": "deepseek-r1-distill-qwen-7b",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful jokester."
            },
            {
                "role": "user",
                "content": "Tell me a joke."
            }
        ],
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": "joke_response",
                "strict": "true",
                "schema": {
                    "type": "object",
                    "properties": {
                        "joke": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "joke"
                    ]
                }
            }
        },
        "temperature": 0.7,
        "max_tokens": 50,
        "stream": False
    }

    response = requests.post(endpoint, payload)

    if response.status_code != 200:
        print("Fail :(")
        sys.exit()
    
    generated_response = response.json()
    answer = generated_response.get("choices")[0].get("message").get("content")

    print(answer)


def get_models():
    endpoint = BASE_URL + 'v1/models'
    response = requests.get(endpoint)

    if response.status_code != 200:
        print("Fail :(")
        sys.exit()

    generated_response = response.json()
    print(generated_response)

post_chat_completions()