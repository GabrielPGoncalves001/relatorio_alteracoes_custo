def regra_coluna_custo_liquido_anterior(df):
    if df is None:
        raise ValueError('Função esperava receber um df mas o valor informado é vazio.\nFunção :: regra_coluna_custo_liquido_anterior')

    if 'VLRCUSTOLIQUIDO' not in df.columns:
        raise KeyError('Coluna de custo líquido não encontrada na tabela informada para esta função.\nFunção :: regra_coluna_custo_liquido_anterior')
    
    try:
        df['CUSTO_LIQUIDO_ANTERIOR'] = (
            df.groupby(['SEQFAMILIA','SEQFORNECEDOR'])
            ['VLRCUSTOLIQUIDO'].shift(-1)
            )
        print('[OK] Dado de custo anterior criado na tabela, com o nome de CUSTO_LIQUIDO_ANTERIOR.')
        return df
    except Exception as e:
        raise RuntimeError(f'Não foi possível criar a coluna de custo liquido anterior na tabela.\nFunção :: regra_coluna_custo_liquido_anterior\n{e}')
    