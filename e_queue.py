from datetime import datetime, timedelta
from random import randint, choice


def is_code_valid(code: str, spec: dict)-> bool:
    return code.upper() in spec['codes_available']


def eq_add_client(eq: dict, idc: int, surname: str, code: str, spec: dict):
    enter = datetime.now()
    timing = timedelta(seconds = randint(5, 10))
    win = choice(spec['win_codes'][code.upper()])
    idc_prev = spec['win_status'][win]
    if idc_prev is None:
        stop = enter + timing
    else:
        stop = eq[idc_prev]['stop'] + timing
    spec['win_status'][win] = idc
    eq[idc] = {'surname': surname, 'code': code.upper(),
               'date': enter,
               'timing': timing,
               'win': win,
               'stop': stop
               }
    return eq, spec


def idc_str(idc: int) -> str:
    return str(idc).zfill(3)


def table_row_str(idc: int, client: dict, spec: dict) -> str:
    date = client['date'].strftime('%d-%m-%y %H:%M:%S')
    surname = client['surname'] if len(client['surname']) <= 10 else client['surname'][:10] + '...'
    sep = spec['output']['sep']
    timing = str(client['timing'])[2:]
    win = client['win']
    result = f"{sep}{idc_str(idc):^{spec['output']['idc_width']}s}{sep}" + \
             f"{surname:^{spec['output']['surname_width']}s}{sep}" + \
             f"{client['code']:^{spec['output']['code_width']}s}{sep}" + \
             f"{date:^{spec['output']['date_width']}s}{sep}" + \
             f"{timing:^{spec['output']['timing_width']}s}{sep}" + \
             f"{win:^{spec['output']['win_width']}s}{sep}"
    return result


def eq_print(eq: dict, version: str, spec: dict) -> None:
    print(f'Электронная очередь. Версия {version}')

    idc_width = spec['output']['idc_width']
    surname_width = spec['output']['surname_width']
    code_width = spec['output']['code_width']
    date_width = spec['output']['date_width']
    timing_width = spec['output']['timing_width']
    win_width = spec['output']['win_width']
    
    total_width = idc_width + surname_width + code_width + date_width + \
                  timing_width + win_width + 7
    print('-' * total_width)
    sep = spec['output']['sep']

    header = f"{sep}{'№':^{idc_width}s}{sep}" + \
             f"{'Фамилия':^{surname_width}s}{sep}" + \
             f"{'Код':^{code_width}s}{sep}" + \
             f"{'Время':^{date_width}s}{sep}" + \
             f"{'Длит.':^{timing_width}s}{sep}" + \
             f"{'Окно':^{win_width}s}{sep}"
    print(header)
    print('-' * total_width)

    for idc, client, in eq.items():
        print(table_row_str(idc, client, spec))
    print('-' * total_width)


def man_cases(number: int) -> str:
    remain = number % 100
    if remain >= 20:
        remain %= 10
    if 2 <= remain <= 4:
        return 'a'
    return ''


def eq_print_footer(eq: dict, spec: dict) -> None:
    lenght = len(eq)
    print(f'Перед вами {lenght} человек{man_cases(lenght)}')
    if lenght != 0:
        mean = sum([client['timing'] for client in eq.values()], start= timedelta(0,0,0,0,0,0))
        mean = str(mean/lenght)[2:7]
        print(f'Среднее время обслуживания {mean}')

def codes_available(spec: dict) -> str:
    return "".join({code for codes in spec['windows'].values() for code in codes})


def windows_by_code(spec: dict) -> dict:
    result = {}
    all_codes = codes_available(spec)
    for code in all_codes:
        result[code] = []
        for window, codes in spec['windows'].items():
            if code in codes:
                result[code].append(window)
    return result


def eq_clear(eq: dict, spec: dict):
    now = datetime.now()
    idc_pop = [idc for idc, client in eq.items() if client['stop'] < now]
    for idc in idc_pop:
        client_win = eq[idc]['win']
        if spec['win_status'][client_win] == idc:
            spec['win_status'][client_win] = None
        eq.pop(idc)
    return eq, spec