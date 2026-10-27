from alteracoes_tabela.extract.query_familias import read_query_familia
from alteracoes_tabela.utils.query_utils import parametros_query
import pandas as pd

def coleta_dados_categoria(df):
    if df is None:
        print('[ERRO] Valor passado como df está vazio na função (coleta_dados_categoria).')

    try:
        params, placeholders = parametros_query(df['SEQFAMILIA'])
    except Exception as e:
        raise RuntimeError(f'Erro tentando coletar os dados para gerar a query com dados de produtos na função coleta_dados_categoria.\n{e}')
    
    if not params or not placeholders:
        raise RuntimeError('Erro tentando gerar os parametros e placeholders da query na função coleta_dados_categoria.')
    
    try:
        df_familia = read_query_familia(params, placeholders)
    except Exception as e:
        raise RuntimeError(f'[ERRO] Erro tentando ler a query com dados de produtos na função coleta_dados_categoria.\n{e}')
    
    if df_familia is None:
        raise ValueError('Tabela gerada pela query de famílias com dados de produtos retornou vazia.')
    try:
        df =  pd.merge(df, df_familia,
                            how='inner',
                            on='SEQFAMILIA')
        print('[OK] Tabela cruzada com a tabela com dados de produtos.')
        return df
    except Exception as e:
        raise RuntimeError(f'Erro tentando cruzar a tabela com a tabela de dados de produto.\nFunção :: coleta_dados_categoria\n{e}')
    
