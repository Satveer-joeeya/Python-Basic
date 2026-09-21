loop1=True
loop2=True
while loop1:
    num1=float(input("Enter your first number : "))
    num2=float(input("Enter your second number : "))
    print("Please select any one operator :- \n 01.ADD(+) \n 02.SUB(-) \n 03.MULT(*) \n 04.DIV(/) \n 05.MOD_DIV(%)")
    choice=int(input("Enter your choice between (01-06) : "))
    if choice==1 :
        add=num1+num2
        print(num1," + ",num2," = ",add)
    elif choice==2 :
        diff=num1-num2
        print(num1," - ",num2," = ",diff)
    elif choice==3 :
        mult=num1*num2
        print(num1," * ",num2," = ",mult)
    elif choice==4 :
        if num2==0:
            print("cannot divide by zero(0) : ")
        else:
            div=num1/num2
            print(num1," / ",num2," = ",div)
    elif choice==5 :
        remain=num1%num2
        print(num1," % ",num2," = ",remain)
    else:
        print("Please Enter right choice B/W (01-06) : ")
    while loop2:
        print("If you want to continue choose 01 otherwise choose 02 : ")
        choose=int(input("Enter your choice B/W (01-02) : "))
        if choose==1:
            loop2 = False
            break
        elif choose==2:
            print("Program Finished !")
            istrue=False
            break
        else:
            print("Please Enter right choice B/W (01-02) : ")