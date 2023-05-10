from datetime import datetime

def main():
    spec = {
        'idc_width':5,
        'surname_width':15,
        'code_width':3,
        'date_width':20,
    }
    idc = 1
    eq = {}
    ver = '3.1'
    codes = 'MNPS'
    while True:
        eq_print(eq, ver, spec)
        print(f'Перед вами {len(eq)} человек.')
        data = input('Введите фамилию или пустая строка для выхода: ')
        if data == '':
            print('Всего вам доброго. До свидания')
            break
        while True:
            code = input(f'Введите код операции. Допустимые коды: {codes}: ')
            if is_code_valid(code, codes):
                break
            else:
                print('Неправильный код операции.')
        eq_add_client(eq, idc, data, code)
        idc += 1


def is_code_valid(code: str, codes: str)-> bool:
    return code.upper() in codes


def eq_add_client(eq:dict, idc:int, surname:str, code:str)-> list:
    eq[idc] = {'surname': surname, 'code': code.upper(), 'date': datetime.now()}
    return eq


def idc_str(idc:int)-> str:
    return str(idc).zfill(3)


def table_row_str(idc:int, client:dict, spec:dict) -> str:
    date = client['date'].strftime('%d-%m-%y %H:%M:%S')
    surname = client['surname'] if len(client['surname']) <= 10 else client['surname'][:10] + '...'
    result = f"|{idc_str(idc):^{spec['idc_width']}s}|" + \
             f"|{surname:^{spec['surname_width']}s}|" + \
             f"|{client['code']:^{spec['code_width']}s}|" + \
             f"|{date:^{spec['date_width']}s}|"
    return result


def eq_print(eq: dict, version: str, spec:dict) -> None:
    print(f'Электронная очередь. Версия {version}')
    total_width = spec['idc_width'] + spec['surname_width'] + spec['code_width'] + spec['date_width'] + 5
    print('-' * total_width)
    for idc, client, in eq.items():
        print(table_row_str(idc, client, spec))
    print('-' * total_width)


if __name__ == "__main__":
    main()