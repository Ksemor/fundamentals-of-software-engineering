import re
text = input("Введите текст: ")
sentences = re.split(r'(?<=[?!.]) ', text)
for i in sentences:
    print(i)
print("Число предложений: ", len(sentences))