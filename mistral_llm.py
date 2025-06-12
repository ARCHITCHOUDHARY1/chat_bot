import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env

def get_mistral_response(prompt):
    api_key = os.getenv("MISTRAL_API_KEY")
    # Use api_key in your logic
    return f"{prompt}"