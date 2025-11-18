text = input("Введите текст: ")
words = text.split()
abbreviature = ""
for i in words:
    if len(i) > 3:
        abbreviature += i[0].upper()
print("Аббревиатура: ", abbreviature)