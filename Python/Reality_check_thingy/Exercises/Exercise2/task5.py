name = "Not set yet"
phone_number = "N/A"
balance = 0


while True:
    choice = int(input("---The Best Bank---\n1.Create an account\n2. Deposit money\n3. Withdraw money\n4. Display account\n5. Exit\n\nEnter Choice:"))
    if choice == 1:
        while True:
            name = input("\n\nEnter your name: ")
            phone_number = input("Enter your phone number: ")
            balance = 0
            print(f'\n\nName: {name}\nPhone number: {phone_number}\nBalance:{balance}\n\n')
            confirm = str(input("Confirm(Y/N): "))
            if confirm == "Y":
                break
            elif confirm == "N":
                continue

    elif choice == 2:
        deposit = int(input("How much would you like to deposit:"))
        balance += deposit
    elif choice == 3:
        withdraw = int(input("How much would you like to withdraw: "))
        balance -= withdraw
    elif choice == 4:
        print(f'\n\nName: {name}\nPhone number: {phone_number}\nBalance:{balance}\n\n')
    elif choice == 5:
        break
    else:
        print ('Error! please try again.')