from datetime import datetime, timedelta
from random import randint

def main():
    data = {'codes': 'MNPS'}
    output = {
        'idc_width': 5,
        'surname_width': 15,
        'code_width': 3,
        'date_width': 20,
        'timing_width': 7,
        'sep': '|'
    }
    spec = {'data': data, 'output': output}
    idc = 1
    eq = {}
    ver = '3.2'

    while True:
        eq_print(eq, ver, spec)
        lenght = len(eq)
        print(f'Перед вами {lenght} человек{man_cases(lenght)}')
        if lenght != 0:
            mean = sum([client['timing'] for client in eq.values()], start= timedelta(0,0,0,0,0,0))
            mean = str(mean/lenght)[2:7]
            print(f'Среднее время обслуживания {mean}')
        data = input('Введите фамилию или пустая строка для выхода: ')
        if data == '':
            raise KeyboardInterrupt
        while True:
            code = input(f"Введите код операции. Допустимые коды: {spec['data']['codes']}: ")
            if is_code_valid(code, spec['data']['codes']):
                break
            else:
                print('Неправильный код операции.')
        eq_add_client(eq, idc, data, code)
        idc += 1


def man_cases(number: int) -> str:
    remain = number % 100
    if remain >= 20:
        remain %= 10
    if 2 <= remain <= 4:
        return 'a'
    return ''


def is_code_valid(code: str, codes: str)-> bool:
    return code.upper() in codes


def eq_add_client(eq: dict, idc: int, surname: str, code: str)-> list:
    eq[idc] = {'surname': surname, 'code': code.upper(),
               'date': datetime.now(),
               'timing': timedelta(seconds = randint(5, 10))}
    return eq


def idc_str(idc: int) -> str:
    return str(idc).zfill(3)


def table_row_str(idc: int, client: dict, spec: dict) -> str:
    date = client['date'].strftime('%d-%m-%y %H:%M:%S')
    surname = client['surname'] if len(client['surname']) <= 10 else client['surname'][:10] + '...'
    sep = spec['output']['sep']
    timing = str(client['timing'])[2:]
    result = f"{sep}{idc_str(idc):^{spec['output']['idc_width']}s}{sep}" + \
             f"{surname:^{spec['output']['surname_width']}s}{sep}" + \
             f"{client['code']:^{spec['output']['code_width']}s}{sep}" + \
             f"{date:^{spec['output']['date_width']}s}{sep}" + \
             f"{timing:^{spec['output']['timing_width']}s}{sep}"
    return result


def eq_print(eq: dict, version: str, spec: dict) -> None:
    print(f'Электронная очередь. Версия {version}')

    idc_width = spec['output']['idc_width']
    surname_width = spec['output']['surname_width']
    code_width = spec['output']['code_width']
    date_width = spec['output']['date_width']
    timing_width = spec['output']['timing_width']

    total_width = idc_width + surname_width + code_width + date_width + timing_width + 6
    print('-' * total_width)
    sep = spec['output']['sep']

    header = f"{sep}{'№':^{idc_width}s}{sep}" + \
             f"{'Фамилия':^{surname_width}s}{sep}" + \
             f"{'Код':^{code_width}s}{sep}" + \
             f"{'Время':^{date_width}s}{sep}" + \
             f"{'Длит.':^{timing_width}s}{sep}"
    print(header)
    print('-' * total_width)

    for idc, client, in eq.items():
        print(table_row_str(idc, client, spec))
    print('-' * total_width)


try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("\nВсего вам доброго. До свидания")