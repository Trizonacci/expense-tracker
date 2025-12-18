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

while True:
    print("\nChoose an option:")
    print("1. Add expense")
    print("2. View expenses")
    print("3. View total")
    print("4. Exit")

    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        add_expense(expenses)
        save_expenses(expenses)

    elif choice == "2":
        print_expenses(expenses)

    elif choice == "3":
        total = calculate_total(expenses)
        print("Total spent:", total)
    elif choice == "4":
        save_expenses(expenses)
        print("Goodbye.")
        break
    else:
        print("invalid choice.")
