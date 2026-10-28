import os
import pandas as pd


def carrega_tabela(df, pasta, nome_arquivo, extensao='xlsx'):
    '''Extensões permitidas: xlsx, csv'''

    dict_decisao = {
        'xlsx':lambda df: df.to_excel(caminho, index=False),
        'csv':lambda df: df.to_csv(caminho,
                                 sep=';',
                                 encoding='latin-1',
                                index=False),
    }

    if df is None:
        raise ValueError('[ERRO] A função (carrega_tabela) esperava receber df sendo uma tabela mas é um objeto vazio.')
    
    if extensao not in dict_decisao:
        raise ValueError('[ERRO] Extensão não permitida.\nFunção :: carrega_tabela')

    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, f'{nome_arquivo}.{extensao}')

    dict_decisao[extensao](df)
    print(f'[OK] Tabela salva como: {caminho}')

def carrega_base_excel(caminho, tabelas):
    with pd.ExcelWriter(caminho,engine='openpyxl') as writer:
        for nome_aba, df in tabelas.items():
            df.to_excel(writer,sheet_name=nome_aba,index=False)