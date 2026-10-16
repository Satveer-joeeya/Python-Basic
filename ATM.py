balance = 10000
pin = 1234
while True:
    enter_pin = int(input("Enter your PIN: "))
    if enter_pin == pin:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your Choice ! ")
        if choice == "1":
            print("Your Bank  Balance = ",balance)
            print("\n Thank you for using ATM ")

        elif choice == "2":
            depo_amount = int(input("Enter your deposit amount: "))

            if depo_amount <= 0:
                print("Please enter a valid amount!")

            else:
                balance += depo_amount
                print(depo_amount, "deposited successfully!")
                print("Available Bank Balance =", balance)

        elif choice == "3":
            withdraw_amount = int(input("Enter withdrawal amount: "))

            if withdraw_amount <= 0:
                print("Please enter a valid amount!")

            elif withdraw_amount > balance:
                print("Insufficient balance!")

            else:
                balance -= withdraw_amount
                print(withdraw_amount, "withdrawn successfully!")
                print("Available Bank Balance =", balance)

        elif choice == "4":
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")