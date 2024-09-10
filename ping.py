from service.generate import generate

def ping():
    body: dict = {
        "prompt": "Respond with 'pong'",
        "temperature": 0,
    }
    res: dict = generate(body)
    msg: str = res["response"]
    total_duration: int = res["total_duration"]
    return msg, total_duration
