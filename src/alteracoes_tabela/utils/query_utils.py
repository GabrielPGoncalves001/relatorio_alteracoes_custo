
def parametros_query(coluna_df):
    placeholders = ', '.join(f':id{i}' for i in range(len(coluna_df)))

    params = {
        f'id{i}': valor
        for i, valor in enumerate(coluna_df)
    }

    return params, placeholders