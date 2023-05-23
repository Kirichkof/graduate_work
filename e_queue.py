

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