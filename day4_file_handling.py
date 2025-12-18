FILE_NAME = "expenses.txt"

def load_expenses():
    expenses = {}

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, amount = line.strip().split(",")
                expenses[name] = float(amount)
    except FileNotFoundError:
        pass 

    return expenses 

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        for name, amount in expenses.items():
            file.write(f"{name}, {amount}\n")

def add_expense(expenses):
    name = input("Enter expense name").strip()
    amount = float(input("Enter expense amount: "))
    
    if amount < 0:
        print("Error: amount cannot be negative")
        return
    if name in expenses:
        expenses[name] += amount
    else:
        expenses[name] = amount

def print_expenses(expenses):
    print("\nexpenses:")
    for name, amount in expenses.items():
        print(f"{name}: {amount}")

def calculate_total(expenses):
    return sum(expenses.values())

expenses = load_expenses()

for i in range(5):
    add_expense(expenses)
print_expenses(expenses)

total = calculate_total(expenses)
print("\nTotal spent:", total)

save_expenses(expenses)