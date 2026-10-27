import numpy as np

def cria_coluna_de_validacao(df, coluna_custo_anterior):
    if df is None:
        raise ValueError('[ERRO] Parâmetro esperado pela função (cria_coluna_de_validacao) esperava um df mas está vazio.')
    
    if not coluna_custo_anterior in df.columns:
        raise KeyError(f'[ERRO] Coluna {coluna_custo_anterior} não encontrada na tabela.\nFunção :: cria_coluna_de_validacao')
    
    if 'VLRCUSTOLIQUIDO' not in df.columns:
        raise KeyError('[ERRO] Coluna "VLRCUSTOLIQUIDO" não encontrada no df.')

    try:    
        df['CONSIDERA'] = np.select(
            [
                (df['VLRCUSTOLIQUIDO'] == df[coluna_custo_anterior]) |
                (df['VLRCUSTOLIQUIDO'] == 0) |
                (df[coluna_custo_anterior] == 0),

                (df['VLRCUSTOLIQUIDO'] != df[coluna_custo_anterior]) &
                (df['VLRCUSTOLIQUIDO'] != 0) 
            ],
            ['N', 'S'],
            default='?'
        )
        print('[OK] Coluna "CONSIDERA" criada na tabela com dados de registros aptos a entrar no relatório.')
        return df
    
    except Exception as e:
        raise RuntimeError(
            f'[ERRO] Erro tentando adicionar a coluna dinamica com base nos registros da tabela para selecinoar registros aptos a entrar no relatório.\nFunção :: cria_coluna_de_validacao\n{e}')