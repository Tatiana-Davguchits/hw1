# 1. Дан список. Выведите те его элементы, которые встречаются в списке только один
# раз. Элементы нужно выводить в том порядке, в котором они встречаются в
# списк

import random

l = [random.randint(1, 10) for i in range(10)]
t = tuple(l)
print(t)

for i in t:
    if t.count(i) == 1:
        print(i, end='')
print()



#3. Даны два кортежа:
# C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
# C_2 = (45, 21,124,76,5,23,91,234)
# Необходимо определить:
# 1) Сумма элементов какого из кортежей больше и вывести соответствующее
# сообщение на экран (Сумма больше в кортеже - ..)
# 2) Вывести на экран порядковые номера минимальных и максимальных элементов
#этих кортежей

C_1 = (35, 78,21,37, 2,98, 6, 100, 231)
C_2 = (45, 21,124,76,5,23,91,234)

C_3 = sum(C_1)
C_4 = sum(C_2)
if C_3 > C_4:
    print('Сумма больше в кортеже - C_1')
else:
    print('Сумма больше в кортеже - C_2')

print('min C_1', min(C_1), 'Номер - ', C_1.index(min(C_1)))
print('max C_1', max(C_1), 'Номер - ', C_1.index(max(C_1)))

print('min C_2', min(C_2), 'Номер - ', C_2.index(min(C_2)))
print('max C_2', max(C_2), 'Номер - ', C_2.index(max(C_2)))



# 4. Создайте словарь из строки ' An apple a day keeps the doctor away' следующим
# образом: в качестве ключей возьмите символы строки, а значениями пусть будут
# числа, соответствующие количеству вхождений данной буквы в строку.

stroka = 'An apple a day keeps the doctor away'

#dictionary = {symbol: stroka.count(symbol) for symbol in stroka}
#print(dictionary)

d = {}
for i in stroka:
    if i.isalpha() and i not in d:
        d[i] = stroka.count(i)
print(d)


# 6. Даны два списка чисел. Посчитайте, сколько чисел содержится одновременно как в
#первом списке, так и во втором

l_1 = set([random.randint(1, 100) for _ in range(10)])
l_2 = set([random.randint(1, 100) for _ in range(10)])
print('Первый список: ', l_1)
print('Второй список: ',l_2)
print('Совподающие числа: ', l_1 & l_2)
print(len(l_1 & l_2))


# l_1 = set([1, 5, 9, 0, 3, 6])
# l_2 = set([4, 7, 3, 8, 2, 1])
# print('Первый список: ', l_1)
# print('Второй список: ',l_2)
# print('Совподающие числа: ', l_1 & l_2)
# print(len(l_1 & l_2))


# 2. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать.

import random

l = [random.randint(1, 10) for i in range(15)]
t = tuple(l)
print(t)

counter = 0
l = []
for i in t:
    if t.count(i) >= 2 and i not in l:
        counter += t.count(i) // 2
        print(i,t.count(i) // 2)
        l.append(i)
print(counter)



#7. Напишите программу, демонстрирующую работу try\except\finally

nam1 = int(input("Введите первое число: "))
nam2 = int(input("Введите второе число: "))
try:
    result = nam1 / nam2
    print('Результат деления: ', nam1 / nam2),
except ZeroDivisionError:
    print('Ошибка деления числа на ноль'),
    print('Введите число заново: ')
else:
    print("Результат в квадрате: ", result ** 2)
finally:
    print('Конец. До свидания!')










