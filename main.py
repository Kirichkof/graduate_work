from datetime import datetime, timedelta
from random import choice
from pathlib import Path
from sys import argv
import e_queue as q
import e_client as c

def main(argv: list):
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
    files = {'log_dir': 'queue_log', 'logfile_template': 'base_log', 'startup_dir': 'startup_files'}
    spec = {'output': output, 'windows': windows, 'files': files}

    idc = 1
    eq = {}
    ver = '5.2'
    spec['codes_available'] = q.codes_available(spec)
    spec['win_codes'] = q.windows_by_code(spec)
    spec['win_status'] = {win: None for win in spec['windows'].keys()}

    
    if len(argv) != 3:
        print(f'Недостаточное кол-во параметров: {len(argv)}')
        return
    
    _, mode, startup_filename = argv
    if mode not in {'random', 'manual'}:
        print(f'Неправильный режим: {mode}')
        return
    startup_file_path = Path(__file__).parent / spec['files']['startup_dir'] / startup_filename
    if startup_file_path.exists():
        for surname, code in q.eq_read_startup(startup_file_path):
            eq, spec = q.eq_add_client(eq, idc, surname, code, spec)
            idc += 1


    try:
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
    except KeyboardInterrupt:
        filename = q.eq_write_logfile(eq, spec)
        print(f'Файл записан в {filename}')
        print("Всего вам доброго. До свидания")


if __name__ == "__main__":
    main(argv)