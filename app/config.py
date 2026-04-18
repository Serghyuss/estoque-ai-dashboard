import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("API Key do Gemini não encontrada!")