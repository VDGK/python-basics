price = int(input("Введите сумму товара: "))
discount = int(input("Введите размер скидки: "))
price_with_discount = price - (price * discount) / 100
print(f"Цена со скидкой составляет: {price_with_discount}")
