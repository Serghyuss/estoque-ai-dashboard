from google import genai
from app.config import GEMINI_API_KEY

# Inicializa cliente Gemini
client = genai.Client(api_key=GEMINI_API_KEY)

def gerar_insights(kpis):
    """
    Gera análise com IA
    """
    prompt = f"""
    Você é um controller sênior especialista em estoque.

    Analise profundamente:

    KPIs:
    {kpis}

    Considere:
    - Capital parado
    - Risco de ruptura
    - Eficiência de estoque

    Seja específico e direto.

    Formato:
    1. Diagnóstico
    2. Riscos críticos
    3. Oportunidades financeiras
    4. Ações recomendadas
    """
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    return response.text