def selecionar_organizar_colunas(df, colunas):
    
    colunas = ['NRODIVISAO','SEQFAMILIA','SEQPRODUTOS','N1','N2','SEQFORNECEDOR',
               'FORNECEDOR','VLRCUSTOLIQUIDO','CUSTO_LIQUIDO_ANTERIOR',
               'VARIACAO_LIQUIDA_ABSOLUTA','VARIACAO_LIQUIDA_PERCENTUAL']
    
    colunas_faltantes = [col for col in colunas
                         if col not in df.columns]
    if colunas_faltantes:
        raise KeyError(f'[ERRO] Algumas colunas obrigatórias para ordenar não estão na tabela: {",".join(colunas_faltantes)}\nFunção :: selecionar_organizar_colunas')
    try:
        df = df[colunas]
        print('[OK] Tabela foi considerada somente as colunas escolhidas e organizadas na ordem determinada.')
        return df
    except Exception as e:
        raise RuntimeError(f'Erro tentando manter a tabela com as colunas solicitadas.\nFunção :: selecionar_organizar_colunas\n{e}')
