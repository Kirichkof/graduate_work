def main():
    eq = []
    ver = '2.1'
    while True:
        eq_print(eq, ver)
        data = input('Введите фамилию или пустая строка для выхода: ')
        if data == '':
            print('Всего вам доброго. До свидания.')
            break
        eq.append(data)

def eq_print(eq: list, version: str) -> None:
    print(f'Электронная очередь. Версия {version}')
    print('*' * 25)
    for client in eq:
        print(f'|{client:^15s}|')
    print('*' * 25)

if __name__ == '__main__':
    main()