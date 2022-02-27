#2) Дан список list=[15,48,'hello',6,19,'world’].
#Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр.
# Если нечётное, то заменить  его на 1 в списке.
#Все слова: посчитать количество гласных и согласных.
#Вывести всё на экран.

#even = 0
#add = 0
#even_sum = 0
#vowel = 'eyuioaёуеыаоэяию'
#vowel_sum = 0
#consonant_sum = 0

while True:
    list = int(input([15,48,'hello',6,19,"world"]))
    if list.isdigit():
        break
    else:
        print('Вы ввели неверно, попробуйте еще раз.')

list_new = []
for i in list:
    list_new.append(int(i))
print(list_new)

for i in list_new:
    if i % 2 == 0 and i != 0:
        even += 1
    else:
        i == 0
        add += 1
print(i)








