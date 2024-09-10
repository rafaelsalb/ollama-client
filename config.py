import os

class Config:
    USE_HTTPS: bool = os.environ.get("USE_HTTPS") or False
    OLLAMA_SERVER_HOST: str = os.environ.get("OLLAMA_SERVER_HOST") or "10.10.0.95:11434"
