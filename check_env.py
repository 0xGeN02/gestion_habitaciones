"""
This script is used to check the environment variables that are set in the .env file.
"""
import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("PYTHONPATH"))
print(os.getenv("DATABASE_URL"))
print(os.getenv("ENCRYPTION_KEY"))
print(os.getenv("SECRET_KEY"))
print(os.getenv("ALGORITHM"))
print(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
