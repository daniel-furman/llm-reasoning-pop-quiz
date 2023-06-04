"""
Util functions for eval_llm notebook
"""

# read openai token
from dotenv import load_dotenv
import os


def configure_openai() -> str:
    load_dotenv()
    openai_key = os.getenv("openai_key")
    return openai_key
