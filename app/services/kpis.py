import pandas as pd

def calcular_kpis(df):
    """
    Calcula KPIs principais
    """
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    df['Stock'] = pd.to_numeric(df['Stock'], errors='coerce')

    df['valor_estoque'] = df['Price'] * df['Stock']

    kpis = {
        "valor_total": df['valor_estoque'].sum(),
        "ticket_medio": df['Price'].mean(),
        "total_skus": len(df),
        "ruptura_pct": (df['Stock'] == 0).mean() * 100
    }

    return kpis, df