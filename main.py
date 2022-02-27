# a = 5             # переменная типа int
# pi = 3.14         #переменная типа float
# s = "Hello, word" #переменная типа string
# t = True          #переменная типа bool
# print (a)
# print (pi)
# print (s)
# print (t)
# print ("передал текст")
#
# a = 10
# b = 3
# c = 10 // 3
# print (c)
#
# i = 2
# str_i = str(i)
#
#
# print (i)
# print (str_i)

 #дз. Вычислить сумму цифр трехзначного числа.

 n = random.randint(100,999)
 print(n)
 c = n % 10
 n = n // 10
 b = n % 10
 a = n // 10
 print(a+b+c)

# import random
#
# print("Использование random.randint() для генерации случайного целого числа")
# print(random.randint(0, 10))
# print(random.randint(0, 7))
# print(random.randint(0, 15))

# import random
# n = random.randint(100,999)
# print(n)
# a = n // 100
# b = (n // 10) % 10
# c = n % 10
# print(a+b+c)
#
#
#
# # Найти уравнение прямой (y=kx+b), проходящей через две известные точки
#
# print("A(x1; y1):")  # Вывод на экран строки "A(x1; y1):"
# x1 = float(input("\tx1 = "))  # \t -- отступ. input останавливает выполнение программы
#                               # до ввода пользователя и возвращает строку.
#                               # float -- приводит строку к дробному числу
# y1 = float(input("\ty1 = "))
#
# print("B(x2; y2):")
# x2 = float(input("\tx2 = "))
# y2 = float(input("\ty2 = "))
#
# print("Equation:")
# k = (y1 - y2) / (x1 - x2)
# b = y2 - k * x2
# print("\ty = %.2f * x + %.2f" % (k, b))  # %.2f говорит о том, что в строку, которая
#                                          # будет выведена на экран, надо встравить дробное
#                                          #  число с 2мя знаками после запятой, которое передано после строки через
#                                          # оператор %. Т.к. таких выражений в строке 2,
#                                          # то числа переданы в скобках.
# print("%f" % k)
# print("%f %f %f" % (k, b, x1))
#
#
#
#
#
# a = int(input("a:"))
# b = int(input())











