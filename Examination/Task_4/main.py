shopping_list = []
title = input("Enter the title: ")
reset = 0

while True:
    choice = input("\n1. Add an item\n2. Print currently added items\n3. Finished\nR.Reset Shopping List\nT. Reset from template\n\nEnter your choice: ")

    if choice == '1':
        item = input("Enter an item: ")
        shopping_list.append(item)
    elif choice == '2':
        print("Currently added items:")
        for i in shopping_list:
            print(f'{i}')
    elif choice == '3':
        print("-" * 20)
        print(f"{title:^20}")
        print("-" * 20)

        for i in shopping_list:
            print(f'{i}')
        if  reset == 0:
            print (f"<< Shopping list was never reset >>")
        else:
            print (f"<< Shopping list was reset {reset} time(s) >>")
        print("")
        break
    elif choice == "R":
        y_n = input("Are you sure (y/n)?: ")
        if y_n == "y":
            shopping_list = []
            reset += 1
    elif choice == 'T':
        while True:
            template = input("1) Sweets template\n2) Fruit template")
            if template == '1':
                shopping_list = ["Dumle", "Japp", "Bilar"]
                reset += 1
                break
            elif template == "2":
                shopping_list = ["Apple", "Pear", "Banana"]
                reset += 1
                break
            else:
                print ("Invalid option, pick 1 or 2")
    else:
        print("Error: Invalid choice, please try again.")