#1. Перемножить все нечётные значения в диапазоне от 1 до 100.
#2. Записать в массив все числа в диапазоне от 1 до 500 кратные 5.
#3. Вывести на экран все чётные значения в диапазоне от 1 до 497.
#4. Дан массив чисел. Если число встречается более двух раз, то добавить его в новый массив.

#1)
pr = 1
for i in range(1, 100, 2):
    pr *= i
print(pr)


#2)
mas = []
for i in range(1, 500, 1):
    if i % 5 == 0:
        mas.append(i)
print(mas)

#3)
for i in range(1, 497, 1):
    if i % 2 == 0:
        print(i)

#4)
mas_1 = [1, 3, 5, 3, 1]
mas_2 = []
for i in mas_1:
     if mas_1.count(i) >= 2:
         mas_2.append(i)
print(mas_2)


# 5)Задание со звездочкой по строкам:
#Определить является ли строка палиндромом. Пример строки И лежу. — Ужели?.

#a = str(И лежу, - Ужели?):
#print(s.lower)








