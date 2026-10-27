def cria_coluna_variacao_percentual(df, coluna_custo_atual, coluna_custo_anterior, nome):
    if df is None:
        raise ValueError('[ERRO] Erro na função (cria_coluna_variacao_percentual), parâmetro df está vazio.')

    colunas_obrigatorias = [coluna_custo_atual, coluna_custo_atual]
    colunas_faltantes = [col for col in colunas_obrigatorias
                         if col not in df.columns]
    if colunas_faltantes:
        raise KeyError(f'[ERRO] colunas {",".join(colunas_faltantes)} não estão na tabela informada.\nFunção :: cria_coluna_variacao_percentual')
    try:
        df[nome] = round(
            (
                ((df[coluna_custo_atual] / df[coluna_custo_anterior]) - 1) * 100
            ),
        2)
        print('[OK] Coluna de variação percentual criada na tabela com sucesso.')
        return df
    except Exception as e:
        raise RuntimeError(f'[ERRO] Erro tentando criar a coluna de variação percentual na tabela.\nFunção :: cria_coluna_variacao_percentual\n{e}')