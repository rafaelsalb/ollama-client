from typing import List
from service.generate import generate

def chat():
    context = []
    while (msg := input('> ')) != 'quit':
        res: dict = generate({
            'prompt': msg,
            'context': context
        })
        print_response(res)
        context: List[int] = res['context']

def print_response(response: dict) -> None:
    res: str = response['response']
    print(f"$ LLAMA 3.1: {res}")
