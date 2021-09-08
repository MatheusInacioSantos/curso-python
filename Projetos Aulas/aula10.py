from datetime import date, time, datetime, timedelta


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.weekday())
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    # criando uma data qualquer
    data_criada = datetime(2018, 6, 20, 15, 20, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    date_string = '01/01/2020 10:20:30'
    # Convertendo data string para datetime
    data_convertida = datetime.strptime(date_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    # Alteração de data (subtração ou soma)
    nova_data = data_convertida - timedelta(days= 365, hours=2, minutes=1, seconds=15)
    print(nova_data)


def trabalhando_com_date():
    data_atual = date.today()
    print(data_atual.strftime('%A %B %Y'))
    # transformando em string
    data_atual_str = data_atual

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    print(type(horario))
    horario_str = horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))

if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()