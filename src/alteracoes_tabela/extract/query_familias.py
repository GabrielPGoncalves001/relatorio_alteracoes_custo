import sys
sys.path.insert(0,r'S:\price\dev\pipelines\BANCO')
from conectar_banco import main_db
import os
import pandas as pd

def read_query_familia(params, placeholders):
    with open(r'src/alteracoes_tabela/database/query_familias.sql', 'r') as f:
        query = f.read()

        query = query.format(placeholders=placeholders)

        with main_db(os.getenv('DB_USER'),os.getenv('DB_PASSWORD'),'prod') as conn:
            df = pd.read_sql(query, conn, params=params)
            return df
