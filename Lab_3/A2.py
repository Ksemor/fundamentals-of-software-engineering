import string
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
special = '*-#'
errors = []
print("Длина пароля – 8 символов")
print("В пароле должны быть заглавные и строчные буквы, цифры и специальные символы: *, - , #")

password = input('Введите пароль: ')

if len(password) != 8:
    errors.append("Длина пароля не равна 8")

if password.lower() == password:
    errors.append("В пароле отсутствуют заглавные буквы")

if password.upper() == password:
    errors.append("В пароле отсутствуют строчные буквы")

if not any(symbol.isdigit() for symbol in password):
    errors.append("В пароле отсутствуют цифры")

if not any(symbol in special for symbol in password):
    errors.append("В пароле отсутствуют специальные символы")

if not all(symbol in allowed for symbol in password):
    errors.append("В пароле используются непредусмотренные символы")


if len(errors) == False:
    print("Надежный пароль")
else:
    for i in errors:
        print(i)


