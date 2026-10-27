import sys
sys.path.insert(0,r'S:\price\RELATORIOS\TABELA_FORNECEDOR')
from src.query import gera_tabela  # type: ignore

def tabela_fornecedor():
    df = gera_tabela()
    return df