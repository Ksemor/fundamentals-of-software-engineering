def rectangle(rows, colums, char):
    for i in range(rows):
        for c in range(colums):
            print(char, end="")
        print()

def right_triangle(rows, char):
    for i in range(rows):
        for c in range(i+1):
            print(char, end="")
        print()

def frame(rows, colums, char):
    for i in range(rows):
        for c in range(colums):
            if i == 0 or c == 0 or i == rows - 1 or c == colums - 1:
                print(char, end="")
            else:
                print(' ', end='')
        print()


try:
    n = int(input("Введите кол-во строк: "))
    m = int(input("Введите кол-во столбцов: "))
except ValueError:
    print("Ошибка! Введите целые числа для размеров.")
    exit()
char = input("Введите символ для рисования: ")

print(f"\nПРЯМОУГОЛЬНИК {n}x{m}:")
rectangle(n, m, char)
    
print(f"\nПРАВЫЙ ТРЕУГОЛЬНИК ({n} строк):")
right_triangle(n, char)
    
print(f"\nРАМКА {n}x{m}:")
frame(n, m, char)

input("\n\nНажмите Enter, чтобы выйти")
    


