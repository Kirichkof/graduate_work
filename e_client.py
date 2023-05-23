def man_cases(number: int) -> str:
    remain = number % 100
    if remain >= 20:
        remain %= 10
    if 2 <= remain <= 4:
        return 'a'
    return ''


def get_surname() -> str:
    return input('Введите фамилию или пустая строка для выхода: ')


def get_codes(codes: str) -> str:
    return input(f"Введите код операции. Допустимые коды: {codes}: ")