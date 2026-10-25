import random as rd

num = rd.randint(100,999)

while True:

    guess = int(input("Enter the three digit number : "))

    if guess > num :
        print("Lower ! \n")

    elif guess < num :
        print("Higher ! \n")

    elif guess == num :
        print("Congratulation ! you win ",guess," is right Guess \n")
        break
    else :
        print("Only three digit allowed !")