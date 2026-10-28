
def parametros_query(coluna_df):
    if len(coluna_df) == 0:
        raise ValueError('[ERRO] na função de utilidades (parametros_query), coluna do dataframe tem 0 registros.')

    placeholders = ', '.join(f':id{i}' for i in range(len(coluna_df)))

    params = {
        f'id{i}': valor
        for i, valor in enumerate(coluna_df)
    }

    return params, placeholders