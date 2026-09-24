shopping_list = []
title = input("Enter the title: ")
items = 0

while True:
    choice = input("\n1. Add an item\n2. Print currently added items\n3. Finished\n\nEnter your choice: ")

    if choice == 1:
        item = input("Enter an item: ")
        shopping_list.append(item)
        item += 1

    elif choice == 2:
        print("Currently added items:")
        for i in shopping_list:
            print(f'{i}')

    elif choice == "S":
        print (f"Currently the list contains {items} item(s)")

    elif choice == 3:
        print("-" * 20)
        print(f"{title:^20}")
        print("-" * 20)

        for i in shopping_list:
            print(f'{i}')
        print("")
        break
    else:
        print("Error: Invalid choice, please try again.")