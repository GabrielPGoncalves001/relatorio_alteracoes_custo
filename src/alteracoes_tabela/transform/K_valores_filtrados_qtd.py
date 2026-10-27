import pandas as pd

def desconsidera_valores_por_quantidade(df, coluna_criterio, qtd_minima):
    if df is None:
        print('[ERRO] Valor passado como df está vazio na função (coleta_dados_categoria).')
        
    lista_repetidos = df[coluna_criterio].value_counts()

    lista_desconsiderar = lista_repetidos[
        lista_repetidos < qtd_minima
    ].index
        
    return df[~df[coluna_criterio].isin(lista_desconsiderar)]