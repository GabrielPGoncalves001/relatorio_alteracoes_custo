def filtra_valores_validos(df, valor):
    if df is None:
        raise ValueError('[ERRO] Função (filtra_valores_validos) esperava receber um df mas o parâmetro é None.')

    if 'CONSIDERA' not in df.columns:
        raise KeyError('[ERRO] Coluna "CONSIDERA" não está presente na tabela informada na função.')

    try:    
        df = df[df['CONSIDERA'] == valor]
        print('[OK] Coluna filtrada apenas para registros onde a coluna "CONSIDERA" for igual a S')
        return df
    except Exception as e:
        raise RuntimeError(f'[ERRO] Erro tentando filtrar a coluna "CONSIDERA" da tabela igual a S.\nFunção :: filtra_valores_validos\n{e}')