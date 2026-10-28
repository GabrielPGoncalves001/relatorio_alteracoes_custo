def remove_valor_zerado(df, coluna):
    if df is None:
        raise ValueError('[ERRO] Tabela informada na função (remove_valor_zerado) está vazio.')

    if coluna not in df.columns:
        raise KeyError(f'[ERRO] Erro na função de utilidades, {coluna} não encontrada na tabela.Função :: remove_valor_zerado')
    return df[df[coluna] != 0]

def desconsidera_nulos(df):
    if df is None:
        raise ValueError('[ERRO] Tabela informada na função (desconsidera_nulos) está vazio.')
    
    info = df.isna().sum()
    df = df.dropna()
    print(f'[OK] Foram removidos {info} valores nulos da tabela.')
    return df
