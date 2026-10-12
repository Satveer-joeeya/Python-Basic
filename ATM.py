
while True:
    balance = 10000
    pin = 1234
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
            depo_amount = int(input("Enter your deposit amount : "))
            if depo_amount > balance:
                print("Entered amount greater than availble amount ! ")
            elif depo_amount < 0:
                print("Please Enter right amount ! ")
            else :
                balance  -= depo_amount
                print("Your amount ",depo_amount , " deposite successfully ")
                print("Availble Bank Balance = ",balance)
                print("\n Thank you for using ATM ")

