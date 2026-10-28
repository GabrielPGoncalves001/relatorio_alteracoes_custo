from conectar_banco import main_db
import pandas as pd
import os

def tabela_fornecedor():
    with open(r'src/alteracoes_tabela/database/TABELA_PMZ.sql', 'r') as f:
        query = f.read()
       
        with main_db(os.getenv('DB_USER'),os.getenv('DB_PASSWORD'),'prod') as conn:
            try:
                df = pd.read_sql(query, conn)
                print('[OK] Tabela fornecedor gerada.')
                return df
            except Exception as e:
                raise RuntimeError(f'[ERRO] Erro tentando gerar a tabela da tabela fornecedor.\nFunção :: tabela_fornecedor\n{e}')


