contact = {}
while True:
    print("Select option between 1-6\n")
    print("\n 1. Add Contact \n 2.View Contact \n 3.Search Contact")
    print("4.Update Contact \n 5.Delete Contact \n 6.Exit")
    choice = input("Enter your choice !")

    if choice == "1":
        name = input("Enter Name : ")
        phone = input("Enter Phone Number : ")
        contact[name]=phone
        print("Contact add Sucessfully ")
