expenses = input("Введите сумму формата \"<руб> руб <коп> коп \": ").strip().lower().split(" ")
if len(expenses) < 3:
    print(f"{int(expenses[0]):.2f} ₽")
elif len(expenses) == 4:
    print(f"{int(expenses[0])}.{int(expenses[2])} ₽")
else:
    print("Некорректный формат суммы")