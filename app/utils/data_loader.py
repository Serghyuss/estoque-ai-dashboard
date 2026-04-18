import pandas as pd

def carregar_csv(file):
    try:
        df = pd.read_csv(file, sep=None, engine='python')
    except Exception as e:
        raise ValueError(f"Erro ao ler CSV: {e}")

    df.columns = df.columns.str.strip()

    return df