shopping_list = []
title = input("Enter the title: ")
fail = 0

while True:
    choice = int(input("\n1. Add an item\n2. Print currently added items\n3. Finished\n\nEnter your choice: "))

    if choice == 1:
        item = input("Enter an item: ")
        while True:
            count = input("How many are there: ")
            if 1 <= int(count) <= 99:
                new_item = f"{item:<10}X{count:>9}"
                shopping_list.append(new_item)
                break
            else:
                fail += 1
                print("ERROR: You must buy at least 1 but not more than 99 of an item. Try again!")
            

    elif choice == 2:
        print("Currently added items:")
        for i in shopping_list:
            print(f'{i}')
    elif choice == 3:
        print("-" * 20)
        print(f"{title:^20}")
        print("-" * 20)

        for i in shopping_list:
            print(f'{i}')
        print(f"You gave a number outside the valid range a total of {fail} time(s)")
        print("")
        break
    else:
        print("Error: Invalid choice, please try again.")