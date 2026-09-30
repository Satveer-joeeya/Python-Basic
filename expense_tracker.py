expenses = []
while True:
    amount = float(input("Enter expense amount: "))
    expenses.append(amount)
    choice = input("Add another expense? (yes/no): ")
    if choice=="no":
        break
print("Your expenses : ",expenses)
print("Total expense : ",sum(expenses))