food = int(input("Введите затраты на еду: "))
transport = int(input("Введите затраты на траспорт: "))
fun = int(input("Введите затраты на развлечения: "))
total = food + transport + fun
average = total / 3
print(f"Общая сумма всех трат: {total}")
print(f"Среднее значение всех трат: {average}")
