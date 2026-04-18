def validar_colunas(df):
    colunas_necessarias = ["Name", "Price", "Stock", "Availability"]

    for col in colunas_necessarias:
        if col not in df.columns:
            raise ValueError(f"Coluna obrigatória ausente: {col}")