from config import Config
import requests

def generate(body: dict):
    protocol: str = "https" if Config.USE_HTTPS else "http"
    host: str = Config.OLLAMA_SERVER_HOST
    body["stream"] = False
    body["model"] = "llama3.1"
    # body["format"] = "json"

    res: requests.Response = requests.post(
        f"{protocol}://{host}/api/generate",
        json=body
    )
    return res.json()
