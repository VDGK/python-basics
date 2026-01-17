import random
rounds = int(input("Введите количество раундов: "))
choices = ["камень", "бумага", "ножницы"]
score_man = 0
score_pc = 0
for round in range(1, rounds + 1):
    choice_man = ""
    while choice_man not in choices:
        choice_man = input("Введите ваш выбор: ").lower().strip()
    print(f"Пользователь выбрал: {choice_man}")
    choice_pc = random.choice(choices)
    print(f"Компьютер выбрал: {choice_pc}")
    if choice_man == choice_pc:
        score_man = 0
        score_pc = 0
    if choice_man == "камень" and choice_pc == "бумага":
        score_man = score_man
        score_pc = score_pc + 1
    if choice_man == "бумага" and choice_pc == "камень":
        score_man = score_man + 1
        score_pc = score_pc
    if choice_man == "камень" and choice_pc == "ножницы":
        score_man = score_man
        score_pc = score_pc + 1
    if choice_man == "ножницы" and choice_pc == "камень":
        score_man = score_man + 1
        score_pc = score_pc
    if choice_man == "бумага" and choice_pc == "ножницы":
        score_man = score_man
        score_pc = score_pc + 1
    if choice_man == "ножницы" and choice_pc == "бумага":
        score_man = score_man + 1
        score_pc = score_pc
if score_man == score_pc:
    print("Ничья")
elif score_man > score_pc:
    print(f"Победил пользователь со счетом: {score_man}:{score_pc}")
else:
    print(f"Победил компьютер со счетом: {score_pc}:{score_man}")