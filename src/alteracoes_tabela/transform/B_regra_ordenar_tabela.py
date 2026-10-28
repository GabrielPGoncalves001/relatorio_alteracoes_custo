def regra_ordenação_df(df, colunas):
    if df is None:
        raise ValueError("[EERO] Parâmetro esperava receber uma tabela mas está vazio.\nFunção :: regra_ordenação_df")

    colunas_obrigatorias = colunas
    colunas_faltantes = [col for col in colunas_obrigatorias
                         if col not in df.columns]
    if colunas_faltantes:
        raise KeyError(f'[ERRO] Algumas colunas obrigatórias para ordenar não estão na tabela: {",".join(colunas_faltantes)}\nFunção :: regra_ordenação_df')

    try:
        df = df.sort_values(
            colunas_obrigatorias,
            ascending=[True, True, False])
        print(f'[OK] Tabela ordenada pelas colunas: {colunas_obrigatorias}.')
        return df
    except Exception as e:
        raise RuntimeError(f'[ERRO] Erro tentando ordenar a tabela pelas colunas: {colunas_obrigatorias}.\nFunção :: regra_ordenação_df\n{e}')