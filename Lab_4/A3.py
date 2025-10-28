while True:
    packets = input("Введите последовательность пакетов данных (0,1): ")

    if len(packets) < 5:
        print("Введите минимум 5 символов")
        continue
    
    if not all(char in "01" for char in packets):
        print("Введен неверный символ")
        continue
    break

all_packets = len(packets)
lost_packets = packets.count('0')

current = 0
max = 0

for i in packets:
    if i == '0':
        current += 1
        if current > max:
            max = current
    else:
        current = 0

percent = (lost_packets / all_packets) * 100

if percent <= 1:
    quality = "Отличное качество"
elif percent <= 5:
    quality = "Хорошее качество"
elif percent <= 10:
    quality = "Удовлетворительное качество"
elif percent <= 20:
    quality = "Плохое качество"
else:
    quality = "Критическое состояние сети"

print(f"\n• Общее количество пакетов: {all_packets}")
print(f"• Количество потерянных пакетов: {lost_packets}")
print(f"• Самая длинная последовательность потерянных пакетов: {max}")
print(f"• Процент потерь: {percent:.1f}%")
print(f"• Качество связи: {quality}")

