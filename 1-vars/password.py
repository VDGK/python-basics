import string
from string import ascii_letters, digits
import random

def generate_password(length: int = 8, use_symbols: bool = True) -> str:
    if length < 3:
        return ""
    password_chars: list[str] = []
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%&*?"
    pool = letters + digits + (symbols if use_symbols else "")
    while len(password_chars) < length:
        password_chars.append(random.choice(pool))
    return "".join(password_chars)

passwords: dict[str, str] = {}

def get_password()  :
    password = input("Введите пароль (пустой пароль для генерации):")
    if password == "":
        password = generate_password()
    return password

def show_passwords(passwords: dict[str, str]) -> dict[str, str]:
    print("Key".ljust(30), "|",  "Value".ljust(30))
    print("-"*60)
    for key, value in passwords.items():
        print(f"{key.ljust(30)} |  {value.ljust(30)}", sep="\n")
    return passwords

def add_password() -> dict[str, str]:
    domain: str = input("Введите домен: ")
    password = get_password()
    passwords[domain] = password
    return show_passwords(passwords)

def delete_password() -> dict[str, str]:
    domain: str = input("Введите домен: ")
    if domain not in passwords:
        print("Такого домена нет")
        return passwords
    passwords.pop(domain)
    print("Пароль удалён")
    return show_passwords(passwords)

def update_password() -> dict[str, str] :
    domain: str = input("Введите домен: ")
    if domain not in passwords:
        print("Такого домена нет")
        return passwords
    password: str = get_password()
    passwords[domain] = password
    print("Пароль обновлен")
    return show_passwords(passwords)

def show_menu():
    print("======== Меню ========")
    menu = ("1. Показать пароли.\n"
            "2. Добавить пароль.\n"
            "3. Удалить пароль.\n"
            "4. Обновить пароль.\n"
            "5. Выход\n"
          )
    print(menu)
    menu_num :str = input("Введите пункт меню: ")
    match menu_num:
        case "1":
            show_passwords(passwords)
        case "2":
            add_password()
        case "3":
            delete_password()
        case "4":
            update_password()
        case _:
            exit()

while True:
    show_menu()
