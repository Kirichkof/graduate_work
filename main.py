from datetime import datetime, timedelta
from random import choice
import e_queue as q
import e_client as c

def main():
    windows = {'win1': 'M', 
               'win2': 'NS', 
               'win3': 'P', 
               'win4': 'N', 
               'win5': 'MS'}
    output = {
        'idc_width': 5,
        'surname_width': 15,
        'code_width': 3,
        'date_width': 20,
        'timing_width': 7,
        'win_width': 6,
        'sep': '|'
    }
    spec = {'output': output, 'windows': windows}

    idc = 1
    eq = {}
    ver = '4.1'

    codes = q.codes_available(spec)
    win_codes = q.windows_by_code(spec)

    while True:
        q.eq_print(eq, ver, spec)
        lenght = len(eq)
        print(f'Перед вами {lenght} человек{c.man_cases(lenght)}')
        if lenght != 0:
            mean = sum([client['timing'] for client in eq.values()], start= timedelta(0,0,0,0,0,0))
            mean = str(mean/lenght)[2:7]
            print(f'Среднее время обслуживания {mean}')
        surname = c.get_surname()
        if surname == '':
            raise KeyboardInterrupt
        while True:
            code = c.get_codes(codes)
            if q.is_code_valid(code, codes):
                break
            else:
                print('Неправильный код операции.')
        win = choice(win_codes[code.upper()])
        q.eq_add_client(eq, idc, surname, code, win)
        idc += 1


try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("\nВсего вам доброго. До свидания")