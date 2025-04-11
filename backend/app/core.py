import os
from dotenv import load_dotenv


load_dotenv()


def get_allow_origins() -> list[str]:
    allow_origins = os.getenv("ALLOW_ORIGINS", "").split(",")
    if allow_origins[0]:
        return allow_origins
    return ["*"]

def get_cors_settings() -> dict[str, list[str] | bool]:
    allow_origins = get_allow_origins()
    return {
        "allow_origins": allow_origins,
        "allow_credentials": True,
        "allow_methods": ["*"],
        "allow_headers": ["*"]
    }