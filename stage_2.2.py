def main():
    idc = 1
    eq = []
    ver = '2.2'
    codes = 'MNPS'
    while True:
        eq_print(eq, ver)
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
    

def eq_add_client(eq:list, idc:int, surname:str, code:str)-> list:
    eq.append([idc, surname.title(), code.upper()])
    return eq


def idc_str(idc:int)-> str:
    return str(idc).zfill(3)


def eq_print(eq: list, version: str) -> None:
    print(f'Электронная очередь. Версия {version}')
    idc_width = 5
    surname_width = 15
    code_width = 3
    total_width = idc_width + surname_width + code_width + 4
    print('-' * total_width)
    for idc, surname, code in eq:
        print(f'|{idc_str(idc):^{idc_width}s}|{surname:^{surname_width}s}|{code:^{code_width}s}|')
    print('-' * total_width)


if __name__ == "__main__":
    main()