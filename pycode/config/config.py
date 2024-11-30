import os
from dotenv import load_dotenv

load_dotenv()

config = {"openai_api_key": os.getenv("OPENAI_API_KEY")}
