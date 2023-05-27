def get_surname() -> str:
    return input('Введите фамилию или пустая строка для выхода: ')


def get_codes(spec: dict) -> str:
    return input(f"Введите код операции. Допустимые коды: {spec['codes_available']}: ")