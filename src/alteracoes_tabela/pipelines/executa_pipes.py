from alteracoes_tabela.extract.query_familias import read_query_familia
from alteracoes_tabela.extract.query_tabela_fornecedor import tabela_fornecedor

from alteracoes_tabela.transform.A_regra_divisao import filtra_divisao
from alteracoes_tabela.transform.B_regra_ordenar_tabela import regra_ordenação_df
from alteracoes_tabela.transform.C_cria_coluna_custo_anterior import define_qtd_custos_alterados
from alteracoes_tabela.transform.D_acrescenta_coluna import coluna_custo_anterior
from alteracoes_tabela.transform.E_cria_coluna_considera import cria_coluna_de_validacao
from alteracoes_tabela.transform.F_filtro_registros_validos import filtra_valores_validos
from alteracoes_tabela.transform.G_filtro_de_datas import filtra_data_pelo_limite
from alteracoes_tabela.transform.H_coluna_variacao_absoluta import cria_coluna_variacao_absoluta
from alteracoes_tabela.transform.I_coluna_variacao_percentual import cria_coluna_variacao_percentual
from alteracoes_tabela.transform.J_formato_numerico import formato_numerico_percetual
from alteracoes_tabela.transform.K_dados_produtos import coleta_dados_categoria
from alteracoes_tabela.transform.L_valores_filtrados_qtd import desconsidera_valores_por_quantidade
from alteracoes_tabela.transform.M_ordenar_colunas import ordena_colunas

from alteracoes_tabela.utils.desconsidera_valores import (remove_valor_zerado, desconsidera_nulos)
from alteracoes_tabela.utils.padronizar_colunas import (padroniza_data, transforma_float, altera_nome_coluna)
from alteracoes_tabela.utils.range_datas import define_range_datas

import pandas as pd
import os

def extract():
    df = tabela_fornecedor()
    return df

def carrega_excel(df, nome):
    caminho = fr'S:\price\RELATORIOS\ALTERACOES_TABELA_COMERCIAL\src\alteracoes_tabela\load\staging\{nome}.xlsx'
    df.to_excel(caminho, index=False)

def transform(df, divisao):
    inicio, fim = define_range_datas(7)
    df = padroniza_data(df)
    df = transforma_float(df, 'VLRCUSTOLIQUIDO')
    df = filtra_divisao(df, divisao)
    df = regra_ordenação_df(df)
    carrega_excel(df, '1_df_raw')

    df_custo_anterior = coluna_custo_anterior(df,'VLRCUSTOLIQUIDO','CUSTO_LIQUIDO_ANTERIOR')
    carrega_excel(df_custo_anterior,'2_df_coluna_custo_anterior')
    
    df_nulos = desconsidera_nulos(df_custo_anterior)
    carrega_excel(df_nulos, '3_df_nulos_desconsiderados')

    df_coluna_validacao = cria_coluna_de_validacao(df_nulos, 'CUSTO_LIQUIDO_ANTERIOR')
    carrega_excel(df_coluna_validacao, '4_df_coluna_validacao')

    df_validacao_filtrada = filtra_valores_validos(df_coluna_validacao)
    carrega_excel(df_validacao_filtrada, '5_df_validacao_filtrada_S')

    df_data_filtrada = filtra_data_pelo_limite(df_validacao_filtrada, inicio, fim)
    carrega_excel(df_data_filtrada,'6_df_data_filtrada')

    df_variacao_absoluta = cria_coluna_variacao_absoluta(df_data_filtrada, 'VLRCUSTOLIQUIDO','CUSTO_LIQUIDO_ANTERIOR','VARIACAO_LIQUIDA_ABSOLUTA')
    df_variacao_percentual = cria_coluna_variacao_percentual(df_variacao_absoluta,'VLRCUSTOLIQUIDO','CUSTO_LIQUIDO_ANTERIOR','VARIACAO_LIQUIDA_PERCENTUAL')
    
    df_nmr_alterado = formato_numerico_percetual(df_variacao_percentual, 'VARIACAO_LIQUIDA_PERCENTUAL')
    df_dados = coleta_dados_categoria(df_nmr_alterado)

    df_qtd_registro = desconsidera_valores_por_quantidade(df_dados, 'SEQFORNECEDOR', 5)
    carrega_excel(df_qtd_registro,'7_df_registros_acima_5')

    df_fim = altera_nome_coluna(df_qtd_registro,'FANTASIA','FORNECEDOR')
    print(df.columns)

    df_pronto = ordena_colunas(df_fim)
    
    return df_pronto

df = extract()
df = transform(df, 1)
print(df.dtypes)
df.to_excel(r'S:\price\TABELA_FORNECEDOR_AJUSTES_DE_PREÇO\alteracoes.xlsx', index=False)