text = input("Введите исходный текст: ")

while True:
    left = text.rfind('(')
        
    if left == -1:
        break
            
    right = text.find(')', left)
        
    if right == -1:
        break
            
    text = text.replace(text[left:right + 1], '')
    
text = ' '.join(text.split())
print("Укороченный текст: ", text)