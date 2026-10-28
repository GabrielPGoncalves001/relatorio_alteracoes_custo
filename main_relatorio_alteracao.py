from src.alteracoes_tabela.pipelines.executa_pipes import extract, transform, load
import time

divisoes = [1, 2]

for i in divisoes:
    nome = 'ALTERACOES_CUSTO_VAREJO' if i == 1 else 'ALTERACOES_CUSTO_ATACADO'

    tentativas = 0

    while tentativas < 3:
        try:
            df = extract()
            df = transform(df, i)
            load(df, nome)

            print(f'[FIM] Pipeline da divisão {i} concluída.')
            break

        except Exception as erro:
            tentativas += 1

            print(f'[ERRO] Tentativa {tentativas}/3 da divisão {i}: {erro}')

            if tentativas < 3:
                print('[INFO] Nova tentativa em 5 segundos...')
                time.sleep(5)
            else:
                print(f'[FALHA] Divisão {i} não concluída após 3 tentativas.')