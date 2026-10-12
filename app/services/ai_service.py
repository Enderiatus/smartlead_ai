import os
from google.genai.errors import APIError
from google import genai
from config import Configs

# Model adı Render'daki GEMINI_MODEL değişkeninden okunur
MODEL = os.environ.get('GEMINI_MODEL', 'gemini-3.5-flash')

try:
    client = genai.Client(api_key=Configs.GEMINI_API_KEY)
except Exception as e:
    print(f"İstemci başlatılırken kritik bir hata oluştu: {e}")
    client = None


def talkWithAI(text):
    if not client:
        return "Sistem demo modunda çalışıyor, lütfen API anahtarınızı kontrol edin."
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=text,
            config={'system_instruction': Configs.BUSINESS_CONTEXT},
        )
        if response and response.text:
            return response.text
        return "Şu an yanıt veremiyorum, lütfen tekrar dene."
    except APIError as api_err:
        print(f"Gemini API Hatası: {api_err}")   # ayrıntı Render loglarına
        return "Şu an yanıt veremiyorum, lütfen tekrar dene."
    except Exception as general_err:
        print(f"Beklenmedik bir hata: {general_err}")
        return "Şu an yanıt veremiyorum, lütfen tekrar dene."
