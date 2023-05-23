from datetime import datetime, timedelta
from random import randint
import e_queue as q
import e_client as c

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
    ver = '4.1'

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


try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("\nВсего вам доброго. До свидания")