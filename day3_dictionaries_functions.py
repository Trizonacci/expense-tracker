def add_expense(expenses):
    name = input("Enter expense")
    amount = float(input("Enter expense amount: "))

    if amount < 0:
        print("Error: amount cannot be negative")
        return
    
    expenses[name] = amount 

def calculate_total(expenses):
    total = 0 
    for amount in expenses.values():
        total += amount
    return total

def print_expenses(expenses):
    print("\nExpenses:")
    for name, amount in expenses.items():
        print(f"{name}: {amount}")

expenses = {}
for i in range(5):
        add_expense(expenses)

print_expenses(expenses)

total = calculate_total(expenses)
print("\nTotal spent:", total)