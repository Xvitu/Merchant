# settings.py
import os
from dotenv import load_dotenv
load_dotenv()

GSE_API_URL = os.getenv('GSE_API_URL')
GSE_SECRET_KEY = os.getenv('GSE_SECRET_KEY')
GSE_ID = os.getenv('GSE_ID')
