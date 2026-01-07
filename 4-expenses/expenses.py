expenses = input("Введите сумму формата \"<руб> руб <коп> коп \": ").strip().lower().split(" ")
if len(expenses) < 3 and expenses[1] == "руб":
    print(f"{int(expenses[0]):.2f} ₽")
elif len(expenses) == 4 and expenses[1] == "руб" and expenses[3] == "коп":
    print(f"{int(expenses[0])}.{int(expenses[2]):.2f} ₽")
else:
    print("Некорректный формат суммы")