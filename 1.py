'''fffff'''

age=int(input('Введите возраст:'))
if age > 0 and age < 7:
    print('Вам в детский сад')
elif 7 <= age < 18:
    print('Вам в школу')
elif age >= 18 and age < 25:
    print('Вам в профессиональное учебное заведение')
elif age >= 25 and age < 60:
    print('Вам на работу')
elif age >= 60 and age < 120:
    print('Вам предоставляется выбор')
elif age < 0 or age > 120:
    print('Ошибка! Это программа для людей!!! '*5)
