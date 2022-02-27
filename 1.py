#Найти самое длинное слово в строке.
word_max = input("Введите строку: ")
max = max(word_max.split(), key=len)
print("Самое длинное слово в строке: ", max)







#Преобразовать текст в список слов с удаление знаков препинания.

text = input('Введите текст: ')
punctuation = "# '!"#$%&\'()*+,,,-./:;<=>?@[\\]^_`{|}~'"
for i in text:
    if i in punctuation:
        change = text.replace(i," ")
print("Текст после удаления знаков препинания:\n "+ change)





























