def filtra_divisao(df, divisao):
    if df is None:
        raise RuntimeError('[ERRO] Parâmetro esperava receber um df mas está vazio.\nFunção :: filtra_divisao')
    
    if 'NRODIVISAO' not in df.columns:
        raise KeyError('[ERRO] Tabela gerada não contém a coluna divisão.\nRevise o df gerado pela query.')
    
    if divisao is None or divisao > 2:
        return "ERRO_AJUSTAVEL", "[ERRO_AJUSTAVEL] numero passado como DIVISÃO não foi reconhecido. Selecione 1 ou 2"

    try:
        df = df[df['NRODIVISAO'] == divisao].copy()
        print(f'Tabela filtrada pela divisão: {"VAREJO" if divisao == 1 else "ATACADO"}')
        return df
    except Exception as e:
        raise KeyError(f'[ERRO] Erro tentando filtrar a divisão.\n{e}')