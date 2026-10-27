from alteracoes_tabela.extract.query_familias import read_query_familia
from alteracoes_tabela.utils.query_utils import parametros_query
import pandas as pd

def coleta_dados_categoria(df):
    params, placeholders = parametros_query(df['SEQFAMILIA'])
    df_familia = read_query_familia(params, placeholders)

    return pd.merge(df, df_familia,
                           how='inner',
                           on='SEQFAMILIA')
    
