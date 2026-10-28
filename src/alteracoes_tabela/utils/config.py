from dotenv import load_dotenv
import os

load_dotenv()

RAW = os.getenv('PATH_RAW')
STAGING = os.getenv('PATH_STAGING')
PROCESSED = os.getenv('PATH_PROCESSED')