def add_expenses(expenses: list[float], value: float) -> list[float]:
    expenses.append(value)
    return expenses

def delete_expense(expenses: list[float], index: int) -> list[float]:
    expenses.pop(index)
    return expenses
def get_total(expenses: list[float]) -> float:
    return sum(expenses)

def get_average(expenses: list[float]) -> float:
    return sum(expenses)/len(expenses)

def print_report(expenses: list[float]) -> str:
    return (f"======= Отчет:=======\n"
            f" {get_total(expenses)}\n")
expenses = []
while True:
    print("======== Меню ========")
    menu = ("1. Добавить расход\n"
            "2. Показать все расходы\n"
            "3. Показать сумму и средний расход\n"
            "4. Удалить расход по номеру\n"
            "5. Показать отчет\n"
            "6. Выход\n"
          )
    print(menu)
    menu_num = int(input("Введите пункт меню: "))
    match menu_num:
        case 1:
            add_expenses()
        case 2:
            get_total()
        case 3:
            get_average()
        case 4:
            delete_expence()
        case 5:
            print_report()
        case 6:
            exit()
