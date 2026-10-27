from datetime import datetime, timedelta

def define_range_datas(qtd_dias):
    hoje = datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    inicio = hoje - timedelta(days=(qtd_dias+1))
    fim = hoje + timedelta(days=1)
    return inicio, fim