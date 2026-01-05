expenses = [300, 450, 550, 1200, 350, 768, 999]
sum_expenses = sum(expenses)
min_expenses = min(expenses)
max_expenses = max(expenses)
avg_expenses = sum_expenses / len(expenses)
expenses_tuple= (min_expenses, max_expenses, sum_expenses)
print(expenses_tuple)