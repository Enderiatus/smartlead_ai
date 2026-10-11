from google.genai.errors import APIError
from google import genai
from config import Configs

try:
    client = genai.Client(api_key=Configs.GEMINI_API_KEY)
except Exception as e:
    print(f"İstemci başlatılırken kritik bir hata oluştu: {e}")
    client = None

def talkWithAI(text):
    if not client:
        return "Sistem demo modunda çalışıyor, lütfen API anahtarınızı kontrol edin."
        
    try:
        interaction = client.interactions.create(
            model="gemini-3.5-flash",
            input=text,
            system_instruction=Configs.BUSINESS_CONTEXT
        )
        if interaction and interaction.output_text:
            return interaction.output_text
        return "Uyarı: Yapay zekadan boş bir yanıt döndü."
    except APIError as api_err:
        return f"Gemini API Hatası: {api_err}"
    except Exception as general_err:
        return f"Beklenmedik bir hata: {general_err}"
