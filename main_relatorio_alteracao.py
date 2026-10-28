from src.alteracoes_tabela.pipelines.executa_pipes import extract, transform, load

df = extract()
df = transform(df, 1)
load(df,'PRIMEIRO_TESTE_ALTERACOES')