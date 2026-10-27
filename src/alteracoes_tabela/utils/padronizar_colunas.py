import pandas as pd

def padroniza_data(df):
    df['DATA_ALTERACAO'] = pd.to_datetime(df['DATA_ALTERACAO'], format='%d-%m-%Y %H:%M:%S')
    return df

def transforma_float(df, coluna):
    df[coluna] = (
        df[coluna]
        .str.replace(',', '.', regex=False)
        .astype(float)
    )
    return df

def altera_nome_coluna(df, nome_coluna_atual, nome_novo):
    altera = {nome_coluna_atual:nome_novo}
    return df.rename(columns=altera)