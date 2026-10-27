
def formato_numerico_percetual(df, coluna_valor):
    df[coluna_valor] = df[coluna_valor].map('{:.2f}%'.format)

    return df
