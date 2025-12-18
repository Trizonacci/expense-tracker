expenses = []
for i in range(5):
    name = input ("enter expense name:")
    amount = float(input("Enter expense amount: "))

    if amount < 0:
        print("Error: amount cannot be negative ")
        exit()
       
    expenses.append(amount)

    print("DEBUG - expenses list:", expenses)

    if len(expenses) == 0:
        print("No expenses entered.")
        exit()
    
    total = sum(expenses)
    average = total / len(expenses)

    print("Expenses:", expenses)
    print("Total spent", total)
    print(" Average expense:", average)