expenses = []

def add_expenses(expenses: list[float], value: float) -> list[float]:
    expenses.append(value)
    return expenses

def delete_expense(expenses: list[float], index: int) -> list[float]:
    if index in range(len(expenses)):
        expenses.pop(index)
    else:
        return expenses
    return expenses
def get_total(expenses: list[float]) -> float:
    return sum(expenses)

def get_average(expenses: list[float]) -> float:
    if len(expenses) == 0:
        return 0.0
    return sum(expenses)/len(expenses)

def print_report(expenses: list[float])
    return print(f"======= Отчет:=======\n"
            f" {get_total(expenses)}\n")
def user_input():
    return int(input("Введите значение: "))

while True:
    print("======== Меню ========")
    menu = ("1. Добавить расход\n"
            "2. Показать сумму\n"
            "3. Показать средний расход\n"
            "4. Удалить расход по номеру\n"
            "5. Показать отчет\n"
            "6. Выход\n"
          )
    print(menu)
    menu_num = int(input("Введите пункт меню: "))
    match menu_num:
        case 1:
            print(add_expenses(expenses, user_input()))
        case 2:
            print(get_total(expenses))
        case 3:
            print(get_average(expenses))
        case 4:
            print(delete_expense(expenses, user_input()))
        case 5:
            print(print_report(expenses))
        case 6:
            exit()
