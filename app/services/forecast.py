def prever_demanda(df):
    """
    Simulação de demanda baseada em heurística simples
    """
    df['demanda_estimada'] = (
        df['Price'].rank(pct=True) * 0.5 +
        (1 - df['Stock'].rank(pct=True)) * 0.5
    ) * 100

    return df