from alteracoes_tabela.extract.query_tabela_fornecedor import tabela_fornecedor

from alteracoes_tabela.transform.A_regra_divisao import filtra_divisao
from alteracoes_tabela.transform.B_regra_ordenar_tabela import regra_ordenação_df
from alteracoes_tabela.transform.C_cria_coluna_custo_anterior import regra_coluna_custo_liquido_anterior
from alteracoes_tabela.transform.D_cria_coluna_considera import cria_coluna_de_validacao
from alteracoes_tabela.transform.E_filtro_registros_validos import filtra_valores_validos
from alteracoes_tabela.transform.F_filtro_de_datas import filtra_df_pelo_range_datas
from alteracoes_tabela.transform.G_coluna_variacao_absoluta import cria_coluna_variacao_absoluta
from alteracoes_tabela.transform.H_coluna_variacao_percentual import cria_coluna_variacao_percentual
from alteracoes_tabela.transform.I_formato_numerico import formato_numerico_percetual
from alteracoes_tabela.transform.J_dados_produtos import coleta_dados_categoria
from alteracoes_tabela.transform.K_valores_filtrados_qtd import desconsidera_valores_por_quantidade
from alteracoes_tabela.transform.L_selecao_colunas import selecionar_organizar_colunas

from alteracoes_tabela.load.carrega_tabelas import carrega_tabela

from alteracoes_tabela.utils.desconsidera_valores import (remove_valor_zerado, desconsidera_nulos)
from alteracoes_tabela.utils.padronizar_colunas import (padroniza_data, transforma_float, altera_nome_coluna)
from alteracoes_tabela.utils.range_datas import define_range_datas

import pandas as pd
import os

def extract():
    df = tabela_fornecedor()
    return df

def transform(df, divisao):
    inicio, fim = define_range_datas(7)
    df = padroniza_data(df,'DATA_ALTERACAO')
    df = transforma_float(df, 'VLRCUSTOLIQUIDO')
    df = filtra_divisao(df, divisao)
    df = regra_ordenação_df(df)

    df = regra_coluna_custo_liquido_anterior(df,'VLRCUSTOLIQUIDO','CUSTO_LIQUIDO_ANTERIOR')
    df = desconsidera_nulos(df)

    df = cria_coluna_de_validacao(df, 'CUSTO_LIQUIDO_ANTERIOR')
    df = filtra_valores_validos(df)

    df = filtra_df_pelo_range_datas(df, inicio, fim)

    df = cria_coluna_variacao_absoluta(df, 'VLRCUSTOLIQUIDO','CUSTO_LIQUIDO_ANTERIOR','VARIACAO_LIQUIDA_ABSOLUTA')
    df = cria_coluna_variacao_percentual(df,'VLRCUSTOLIQUIDO','CUSTO_LIQUIDO_ANTERIOR','VARIACAO_LIQUIDA_PERCENTUAL')
    
    df = formato_numerico_percetual(df, 'VARIACAO_LIQUIDA_PERCENTUAL')
    df = coleta_dados_categoria(df)

    df = desconsidera_valores_por_quantidade(df, 'SEQFORNECEDOR', 5)

    df = altera_nome_coluna(df,'NOMERAZAO','FORNECEDOR')

    df = selecionar_organizar_colunas(df,
                                    ['NRODIVISAO','SEQFAMILIA','SEQPRODUTOS','N1','N2','SEQFORNECEDOR',
                                    'FORNECEDOR','VLRCUSTOLIQUIDO','CUSTO_LIQUIDO_ANTERIOR',
                                    'VARIACAO_LIQUIDA_ABSOLUTA','VARIACAO_LIQUIDA_PERCENTUAL'])
    
    return df

def load(df):
    pasta = r'S:\price\RELATORIOS\ALTERACOES_TABELA_COMERCIAL\src\alteracoes_tabela\data\processed'
    carrega_tabela(df)