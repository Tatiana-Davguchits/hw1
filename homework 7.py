#1.Матрица 5 х 5. Найти строку с максимальной суммой элементов и вывести её номер.

import random
a = []
m = 0
for i in range(5):
    a.append([])
    for j in range(5):
        a[i].append(random.randint(10,99))
        print(a[i][j], end=' ')
    print()
    m = sum(a[i]) if sum(a[i]) > m else m
print(m)


# 2.Ввод с клавиатуры. Если строка введённая с клавиатуры – это числа, то поделить первое на
# второе. Обработать ошибку деления на ноль. Если второе число 0, то программа
# запрашивает ввод чисел заново. Также если были введены буквы, то обработать
# исключение.

nam1 = int(input("Введите первое число: "))
nam2 = int(input("Введите второе число: "))
try:
    result = nam1 / nam2
    print('Результат деления: ', nam1 / nam2),
except ZeroDivisionError:
    print('Ошибка деления числа на ноль'),
    print('Введите число заново')
except ValueError:
    print('Вы ввели буквы '),
else:
    print('Введите число заново: ')










