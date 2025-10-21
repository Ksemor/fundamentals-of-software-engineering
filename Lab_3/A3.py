prev_month = int(input("Введите показание счетчика в предыдущем месяце: "))
this_mounth = int(input("Введите показание счетчика в этом месяце: "))

gas = (this_mounth - prev_month + 10000) % 10000

if gas <= 300:
    value = 21
elif gas > 300 and gas <= 600: 
    value = 21 + (gas - 300) * 0.06
elif gas > 600 and gas <= 800:
    value = 21 + 300 * 0.06 + (gas - 600) * 0.04
elif gas > 800:
    value = 21 + 300 * 0.06 + 200 * 0.04 + (gas - 800) * 0.025
value_m3 = value/gas
value1 = round(value, 2)
value_m31 = round(value_m3, 2)


print("\nОбъем газа в прошлом месяце: ", prev_month)
print("\nОбъем газа в этом месяце: ", this_mounth)
print("\nИспользовано: ", gas)
print("\nК оплате: ", value1, "$")
print("\nСр. цена m^3: ", value_m31, "$")

