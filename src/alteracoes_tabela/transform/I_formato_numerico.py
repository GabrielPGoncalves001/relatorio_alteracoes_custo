
def formato_numerico_percetual(df, coluna_valor):
    if df is None:
        raise ValueError('[ERRO] Erro na função (formato_numerico_percetual), parâmetro df está vazio.')
    
    if coluna_valor not in df.columns:
        raise KeyError(f'[ERRO] Coluna {coluna_valor} não encontrada na tabela informada na função.')

    #if not isinstance(coluna_valor,int) or isinstance(coluna_valor,float):
        #raise TypeError('[ERRO] Esperava-se uma coluna com valores do tipo numérico (float ou int).\nFunção :: formato_numerico_percentual')

    try:
        df[coluna_valor] = df[coluna_valor].map('{:.2f}%'.format)
        print(f'[OK] coluna {coluna_valor} alterado o formato numérico para 2 casas decimais com %.')
        return df
    except Exception as e:
        raise RuntimeError(f'Erro tentando alterar o formato da coluna {coluna_valor}.Função :: formato_numerico_percetual\n{e}')
