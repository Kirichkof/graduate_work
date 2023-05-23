def man_cases(number: int) -> str:
    remain = number % 100
    if remain >= 20:
        remain %= 10
    if 2 <= remain <= 4:
        return 'a'
    return ''