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

    elif choice == "2":
        if len(contact)==0:
            print("No contact found !")
        else:
            print("Contact : ")
            for name,phone in contact.items():
                print(name," : ",phone)

    elif choice == "3":
        name=input("Search by name : ")
        if name in contact:
            print(name," : ",contact[name])
        else:
            print("Contact not Found ! ")

    elif choice == "4":
        name = input("Enter name to update: ")
        if name in contact:
            phone = input("Enter new phone number: ")
            contact[name] = phone
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        name = input("Enter name to delete: ")
        if name in contact:
            del contact[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")
    elif choice == "6":
        print("Thank you for using contact book ")
        break
    else:
        print(" 'Invalid input ' please enter choice bitween 1-6 ! ")