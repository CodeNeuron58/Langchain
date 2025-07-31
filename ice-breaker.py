import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

if __name__=="__main__":
    print("hello")
    print(os.environ["OPEN_AI_KEY"])