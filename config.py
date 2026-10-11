import os
from dotenv import load_dotenv
load_dotenv()

class Configs:
    AI_PROVIDER = os.environ.get('AI_PROVIDER')
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    DATABASE_URL = os.environ.get('DATABASE_URL')
    BUSINESS_CONTEXT = os.environ.get('BUSINESS_CONTEXT', 'OtoWise AI Satış Danışmanı')
    CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS', '*')
