def filtra_divisao(df, divisao):
    if df is None:
        raise RuntimeError('[ERRO] Parâmetro esperava receber um df mas está vazio.\nFunção :: filtra_divisao')
    
    if 'NRODIVISAO' not in df.columns:
        raise KeyError('[ERRO] Tabela gerada não contém a coluna divisão, revise o df gerado pela query.\nFunção :: filtra_divisao')
    
    if divisao is None or divisao > 2:
        raise ValueError('[ERRO] Divisão maior que 2 não está permitido para este relatório.\nFunção :: filtra_divisao')

    try:
        df = df[df['NRODIVISAO'] == divisao].copy()
        print(f'[OK] Tabela filtrada pela divisão: {"VAREJO" if divisao == 1 else "ATACADO"}')
        return df
    except Exception as e:
        raise KeyError(f'[ERRO] Erro tentando filtrar a divisão.\n{e}')