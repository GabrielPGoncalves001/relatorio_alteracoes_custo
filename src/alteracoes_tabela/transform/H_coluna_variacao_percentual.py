def cria_coluna_variacao_percentual(df, coluna_custo_atual, coluna_custo_anterior, nome):
    df[nome] = round(
        (
            ((df[coluna_custo_atual] / df[coluna_custo_anterior]) - 1) * 100
        ),
    2)
    
    return df