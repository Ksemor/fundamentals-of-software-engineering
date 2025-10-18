x1 = float(input("Введите x1: "))
x2 = float(input("Введите x2: "))
y1 = float(input("Введите y1: "))
y2 = float(input("Введите y2: "))

if (x1 == 0 or x2 == 0 or y1 == 0 or y2 == 0):
   print ("Какая-то из координат равна нулю") 

elif (x1 > 0 and x2 > 0 and y1 > 0 and y2 > 0):
    print ("Да, в 1 четверти")
elif (x1 < 0 and x2 < 0 and y1 > 0 and y2 > 0):
    print ("Да, в 2 четверти")
elif (x1 < 0 and x2 < 0 and y1 < 0 and y2 < 0):
    print ("Да, в 3 четверти")
elif (x1 > 0 and x2 > 0 and y1 < 0 and y2 < 0):
    print ("Да, в 4 четверти")
else:
    print ("Нет")