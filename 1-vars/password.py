import string
from string import ascii_letters, digits
import random

def generate_password(length: int = 8, use_symbols: bool = True) -> str:
    if length < 3:
        return ""
    password_chars: list[str] = []
    if use_symbols:
        pool = string.ascii_letters + string.digits + "!@#$%&*?"
    else:
        pool = string.ascii_letters + string.digits
    while len(password_chars) < length:
        password_chars.append(random.choice(pool))
    return "".join(password_chars)

print(generate_password(10, False))
