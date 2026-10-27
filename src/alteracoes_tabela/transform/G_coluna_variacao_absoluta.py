def cria_coluna_variacao_absoluta(df, coluna_custo_atual, coluna_custo_anterior, nome):
    df[nome] = round(df[coluna_custo_atual] - df[coluna_custo_anterior], 2)
    
    return df