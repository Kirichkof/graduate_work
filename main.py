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
        'stop_width': 20,
        'sep': '|'
    }
    spec = {'output': output, 'windows': windows}

    idc = 1
    eq = {}
    ver = '4.2'
    spec['codes_available'] = q.codes_available(spec)
    spec['win_codes'] = q.windows_by_code(spec)
    spec['win_status'] = {win: None for win in spec['windows'].keys()} 

    while True:
        eq, spec = q.eq_clear(eq, spec)
        q.eq_print(eq, ver, spec)
        q.eq_print_footer(eq, spec)
        surname = c.get_surname()
        if surname == '':
            raise KeyboardInterrupt
        while True:
            code = c.get_codes(spec)
            if q.is_code_valid(code, spec):
                break
            else:
                print('Неправильный код операции.')
        eq, spec = q.eq_clear(eq, spec)
        eq, spec = q.eq_add_client(eq, idc, surname, code, spec)
        idc += 1


try:
    if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("\nВсего вам доброго. До свидания")