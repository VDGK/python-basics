# users = [{"name": "  anton " , "age" : "25"},
#          {"name": "KATE" , "age" : " 30 "},
#          {"name": "Oleg" , "age" : "22"}]

# def normalize(user: dict[str ,str]) -> dict:
#     return {
#         "name": user["name"].strip().capitalize(),
#         "age": int(user["age"].strip())
#     }

# normalizer_user = list(map(normalize,users))
# print(normalizer_user)

# orders = [
#     {"id": 1, "user": "Anton", "amount": 150, "status": "paid"},
#     {"id": 2, "user": "Kate", "amount": 50, "status": "canceled"},
#     {"id": 3, "user": "Oleg", "amount": 200, "status": "paid"},
#     {"id": 4, "user": "Ivan", "amount": 0, "status": "draft"},
#     {"id": 5, "user": "Maria", "amount": 120, "status": "paid"}
#     ]

# def filtering_orders(order: dict) -> bool:
#     if order["amount"] > 100 and order["status"] == "paid":
#         return True
#     return False

# filtered_orders = list(filter(filtering_orders, orders))
# filtered_orders = list(filter(lambda order: order["amount"] > 100 and order["status"] == "paid", orders))

# print(filtered_orders)


# from functools import reduce


# orders = [
#     {"id": 1, "user": "Anton", "items": [
#         {"name": "Laptop", "price": 1000},
#         {"name": "Mouse", "price": 50}
#     ]},
#     {"id": 2, "user": "Kate", "items": [
#         {"name": "Phone", "price": 700}
#     ]},
#     {"id": 3, "user": "Oleg", "items": [
#         {"name": "Monitor", "price": 300},
#         {"name": "Keyboard", "price": 100}
#     ]}
# ]

# def aggregate(acc: dict, order: dict) -> dict:
#     order_sum = 0
#     for item in order["items"]:
#         order_sum += item["price"]
#     order_items = len(order["items"])
#     return {
#         "total_price": acc["total_price"] + order_sum,
#         "total_items": acc["total_items"] + order_items
#         }

# result = reduce(aggregate, orders, {"total_price": 0, "total_items": 0})
# print(result)

# from functools import reduce

# employees = [
#     {"name": "Anton", "departament": "IT", "salary": 120000, "active": True},
#     {"name": "Kate", "departament": "HR", "salary": 90000, "active": False},
#     {"name": "Oleg", "departament": "IT", "salary": 150000, "active": True},
#     {"name": "Maria", "departament": "Finance", "salary": 110000, "active": True},
#     {"name": "Ivan", "departament": "IT", "salary": 95000, "active": False},
#     {"name": "Dasha", "departament": "Finance", "salary": 130000, "active": True}
#     ]

# filtered_employees = list(filter(lambda e: e["name"] and e["salary"] and e["active"], employees))
# sorted_salary = list(sorted(filtered_employees, key=lambda e : -e["salary"]))
# summary_bill = reduce(lambda acc, e: acc + e["salary"], sorted_salary, 0)

# print(summary_bill)

# def apply_to_list(func, items):
#     new_list = []
#     for item in items:
#         new_list.append(func(item))
#     return new_list

# test_data = [1, 2, 3, 4]
# double_func = lambda x: x * 2

# print(apply_to_list(double_func, test_data))

# def filter_and_transform(filter_func, transform_func, items):
#     transform_list = []
#     for i in items:
#         if filter_func(i):
#             transform_list.append(transform_func(i))
#     return transform_list

# result1 = filter_and_transform(lambda x: x > 5, lambda x: x * 2, [3, 7, 2, 9, 1, 8])
# print(result1)

# result2 = filter_and_transform(lambda x: len(x) > 3, lambda x: x.upper(), ['cat', 'elephant', 'dog', 'tiger'])
# print(result2)

# def make_counter():
#     count = 0
#     def counter():
#       nonlocal count
#       count += 1
#       return count
    
#     return counter

# counter_a = make_counter()
# print(counter_a())

# def reduce_with_initial(reducer_func, initial, items):
#     for i in items:
#         initial = reducer_func(initial, i)
#     return initial

# # Примеры для тестирования:
# print(reduce_with_initial(lambda acc, x: acc + x, 0, [1, 2, 3, 4]))
# print(reduce_with_initial(lambda acc, x: acc + ' ' + x, 'start', ['hello', 'world']))

def partial_apply(func, first_arg):
    def second_func(second_arg):
        return second_arg
    return second_func

result = partial_apply(lambda x, y: x * y, 3)
print(result)