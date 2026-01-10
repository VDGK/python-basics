# expenses = input("Введите сумму формата \"<руб> руб <коп> коп \": ").strip().lower().split(" ")
# if len(expenses) < 3 and expenses[1] == "руб":
#     print(f"{int(expenses[0]):.2f} ₽")
# elif len(expenses) == 4 and expenses[1] == "руб" and expenses[3] == "коп":
#     print(f"{int(expenses[0])}.{int(expenses[2]):.2f} ₽")
# else:
#     print("Некорректный формат суммы")
while True:
    print("======== Меню ========")
    menu = ("1. Добавить расход\n"
            "2. Показать все расходы\n"
            "3. Показать сумму и средний расход\n"
            "4. Удалить расход по номеру\n"
            "5. Выход\n"
          )
    print(menu)
    menu_num = int(input("Введите пункт меню: "))
    match menu_num:
        case 1:
            add_expenses()
        case 2:
            show_all_expenses()
        case 3:
            show_sum_and_avg()
        case 4:
            delete_expenses_by_id()
        case 5:
            exit()
