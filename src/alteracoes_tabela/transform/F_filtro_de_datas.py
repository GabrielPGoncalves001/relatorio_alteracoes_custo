def filtra_data_pelo_limite(df, data_inicio, data_fim):
    return df[
        (df['DATA_ALTERACAO'] >= data_inicio) &
        (df['DATA_ALTERACAO'] <= data_fim)]