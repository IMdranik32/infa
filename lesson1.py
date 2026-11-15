steps_in_part = 0
floor = 0
total_seconds = 0

PARTS_IN_FLOOR = 2
SEC_LIVE_IN_STEP = 10

print("Данная программа считает на сколько секунд увеличивается ваша жизнь при поднятии пешком на этаж на котором вы живёте")
steps_in_part = int(input("Введите количество ступенек в пролёте:"))
floor = int(input("Введите этаж на котором вы живёте:"))
total_seconds = steps_in_part * PARTS_IN_FLOOR * floor * SEC_LIVE_IN_STEP
print(f"Ваша жизнь при поднятии на {floor} этаж увеличилась на {total_seconds} секунд")