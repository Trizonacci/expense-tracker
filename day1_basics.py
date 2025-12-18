expense_name = input("Enter expense name: ")
amount = float(input("Enter expense amount: "))
if amount < 0: 
    print("Error: amount cannot be negative")
    exit()
elif amount < 20:
    category = "Cheap"
elif amount <= 100:
    category = "Normal" 
else: 
    category = "Expensive"

print("Expense:", expense_name)
print("Amount:", amount)
print("Category:", category)