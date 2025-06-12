import os
from dotenv import load_dotenv

load_dotenv()

def get_sarvam_response(prompt):
    api_key = os.getenv("SARVAM_API_KEY")
    # Replace with real API call
    return f"{prompt}"