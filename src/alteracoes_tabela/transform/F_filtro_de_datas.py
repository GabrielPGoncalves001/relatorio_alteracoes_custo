from datetime import datetime

def filtra_df_pelo_range_datas(df, data_inicio:datetime, data_fim:datetime):
    if df is None:
        raise ValueError('[ERRO] parâmetro informado como df na função (filtra_df_pelo_range_datas) é um objeto vazio.')

    if data_inicio is None or data_fim is None:
        raise ValueError('[ERRO] Dados de data não podem ser informados como vazias.\nFunção :: filtra_df_pelo_range_datas')
    
    if data_inicio > data_fim:
        raise ValueError('[ERRO] A data fim informada é menor que a data inicio.\nFunção :: filtra_df_pelo_range_datas')
    
    if 'DATA_ALTERACAO' not in df.columns:
        raise KeyError('[ERRO] coluna "DATA_ALTERACAO" não encontrada na tabela informada.\nFunção :: filtra_df_pelo_range_datas')

    if not isinstance(data_inicio, datetime) or not isinstance(data_fim, datetime):
         raise TypeError('[ERRO] As variáveis data_inicio e data_fim deveriam ser do tipo datetime.\nFunção :: filtra_df_pelo_range_datas')
    try:
        df = df[
            (df['DATA_ALTERACAO'] >= data_inicio) &
            (df['DATA_ALTERACAO'] <= data_fim)]
        print(f'[OK] Tabela filtrada pelo range data: de {data_inicio} até {data_fim}.')
    except Exception as e:
        raise RuntimeError(f'[ERRO] Erro tentando filtrar a tabela pelo range de data estabelecido.\nFunção :: filtra_df_pelo_range_datas\n{e}')