# Есть массив состоящий из слов и чисел, нужно записать в файл сначала
# слова в порядке их длины, а после слов цифры в порядке возрастания

myword = int,input(['снег', 12, 'дождь', 3, 'солнце', 7, 'мороз', 1])
word_1 = open('hw.txt', 'w')
word_1.writelines(myword)
word_1.close()

file = open('hw.txt' 'r')
stroka = file.readlines()
file.close()
print(stroka)

word = []
numbers = []
for i in stroka:
    i.replace('\n', '')
    if i.isalpha():
        i = str(i)
        word.append(i)
    elif i.isdigit():
        i = int(i)
        numbers.append(i)
print(word)

print(numbers)

word.sort()
numbers.sort()

mas = word + numbers
print(mas)

