def remove_valor_zerado(df, coluna):
    return df[df[coluna] != 0]

def desconsidera_nulos(df):
    return df.dropna()
