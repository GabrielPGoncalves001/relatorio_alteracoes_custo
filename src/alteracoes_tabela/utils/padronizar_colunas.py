import pandas as pd

def padroniza_data(df, coluna_data, format=None):
    padrao = '%d-%m-%Y %H:%M:%S'
   
    if df is None:
        raise ValueError('[ERRO] Erro na função de utilidades (padroniza_data), parâmetro que deveria ser tabela é um objeto vazio.')

    if coluna_data not in df.columns:
        raise KeyError(f'[ERRO] Erro na função de utilidades (padroniza_data), {coluna_data} não encontrada na tabela informada.')
    
    if format:
        try:
            df[coluna_data] = pd.to_datetime(df[coluna_data], format=format)
            print(f'[OK] Coluna de data {coluna_data} da tabela foi alterada para o formato {format}')
            return df
        except (ValueError, TypeError) as erro:
            raise ValueError(
                f"[ERRO] Erro ao converter a coluna '{coluna_data} para datetime usando o formato '{format}':\nFunção :: padroniza_data\n{erro}"
            ) from erro

    try:
        df[coluna_data] = pd.to_datetime(df[coluna_data], format=padrao)
        print(f'[OK] Coluna de data {coluna_data} da tabela foi alterada para o formato padrão: {padrao}')
        return df
    except (ValueError, TypeError) as e:
        raise ValueError(
                f"[ERRO] Erro ao converter a coluna '{coluna_data} para datetime usando o formato '{format}':\nFunção :: padroniza_data\n{erro}"
            ) from e

def transforma_float(df, coluna):
    if df is None:
        raise ValueError('[ERRO] Erro na função de utilidades (transforma_float), parâmetro que deveria ser tabela é um objeto vazio.')

    if coluna not in df.columns:
        raise KeyError(f'[ERRO] Erro na função de utilidades (transforma_float), coluna {coluna} não existe na tabela informada.')

    try:
        df[coluna] = (
            df[coluna]
            .str.replace(',', '.', regex=False)
            .astype(float)
        )
        print(f'[OK] Coluna {coluna} alterada para o time float.')
        return df
    except Exception as e:
        raise RuntimeError(f'[ERRO] Erro tentando converter o tipo da coluna {coluna} para float.\nFunção :: transforma_float\n{e}')
    
def altera_nome_coluna(df, nome_coluna_atual, nome_novo):
    if df is None:
        raise ValueError('[ERRO] Erro na função de utilidades (altera_nome_coluna), parâmetro que deveria ser tabela é um objeto vazio.')

    if nome_coluna_atual not in df.columns:
        raise KeyError(f'[ERRO] Erro na função de utilidades (altera_nome_coluna), a coluna {nome_coluna_atual} não existe na tabela informada.')
    
    altera = {nome_coluna_atual:nome_novo}
    
    try:
        df = df.rename(columns=altera)
        print(f'[OK] nome da coluna {nome_coluna_atual} alterada para: {nome_novo}')
        return df
    except Exception as e:
        raise RuntimeError(f'[ERRO] Erro tentando alterar o nome da coluna {nome_coluna_atual}.\nFunção :: altera_nome_coluna\n{e}')