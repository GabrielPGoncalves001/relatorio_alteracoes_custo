import numpy as np

def cria_coluna_de_validacao(df, coluna_custo_anterior):
    df['CONSIDERA'] = np.select(
        [
            (df['VLRCUSTOLIQUIDO'] == df[coluna_custo_anterior]) |
            (df['VLRCUSTOLIQUIDO'] == 0) |
            (df[coluna_custo_anterior] == 0),

            (df['VLRCUSTOLIQUIDO'] != df[coluna_custo_anterior]) &
            (df['VLRCUSTOLIQUIDO'] != 0) 
        ],
        ['N', 'S'],
        default='?'
    )
    return df