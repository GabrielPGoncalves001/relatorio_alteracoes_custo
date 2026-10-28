import pandas as pd

def desconsidera_valores_por_quantidade(df, coluna_criterio, qtd_minima):
    if df is None:
        print('[ERRO] Valor passado como df está vazio na função (desconsidera_valores_por_quantidade).')

    if coluna_criterio not in df.columns:
        raise KeyError('[ERRO] Coluna não encontrada na tabela informada.\nFunção :: desconsidera_valores_por_quantidade')   

    if qtd_minima <= 0:
        raise ValueError('[ERRO] Quantidade mínima não pode ser igual ou menor que 0.\nFunção :: desconsidera_valores_por_quantidade')
    
    lista_repetidos = df[coluna_criterio].value_counts()

    lista_desconsiderar = lista_repetidos[
        lista_repetidos < qtd_minima
    ].index
    try:
        df = df[~df[coluna_criterio].isin(lista_desconsiderar)]
        print(f'[OK] Tabela filtrada por valores que se repetem no mínimo: {qtd_minima} vezes.')
        return df
    except Exception as e:
        raise RuntimeError(f'[ERRO] Erro tentando filtrar a tabela pela quantidae mínima informada.\nFunção :: desconsidera_valores_por_quantidade\n{e}')