#1.У вас есть словарь, где ключ – название продукта. Значение –
#список, который содержит цену и кол-во товара.
#Выведите через ‘’–’’ название – цену – количество.
#С клавиатуры вводите название товара и его кол-во. n – выход
#из программы. Посчитать цену выбранных товаров и сколько
#товаров осталось в изначальном списке.

goods = {"Apple": [4.5, 10],
         "Orange": [6.2, 5],
         "Pineapple": [10.0, 1],
         "Mango": [7.5, 2],
         "Banana": [3.8, 10]}

for key, value in goods.items():
    print(key, '-', value[0], '-', value[1])

cost = 0
while True:
    good = input("What? (n - nothing) ")
    if good == 'n' or good not in goods.keys():
        break
    qty = int(input("How many? "))
    if qty > goods[good][1]:
        print("We don't have so much.")
        continue
    cost += goods[good][0] * qty
    goods[good][1] -= qty

print("Price:", cost)
print('___________________________________')
for key, value in goods.items():
    print(key, '-', value[0], '-', value[1])








#2. Имеется список с произвольными данными.
# Поставлена задача преобразовать его во множество.
# Если какие-то элементы не неизменяемые, то пропускаем их.
# Вывести на экран полученное множество

lst = [1, [2], False, frozenset([1, 2]), {1, 2, 3},
       (2, 2), 'string', 5.11]
# tuple_type = (int, float, str, bool, tuple, frozenset)
# st = {item for item in lst if type(item) in tuple_type}

st = set()

for item in lst:
    if type(item) in (int, float, str, bool, tuple, frozenset):
        st.add(item)

print(st)




