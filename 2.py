num = int(input('Введите целое число от 1 до 9: '))
if num > 0 and num < 4:
    a = input('Введите строку: ')
    n = int(input('Введите число повторов от 1 до 9: '))
    for value in range(1, n+1):
        print(a)
elif num >= 4 and num < 7:
    m = int(input('Введите число для возвдения в степень от 1 до 9: '))
    if m > 0 and m < 10:
        print(num**m)
    else: print('Ошибка!'*5)
elif num >= 7 and num < 10:
    for chislo in range (1, 11):
        print(chislo+num)
else: print('Ошибка!!!'*5)
