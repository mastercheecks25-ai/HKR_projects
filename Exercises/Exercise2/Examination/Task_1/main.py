shopping_list = []
title = input("Enter the title: ")
cost = float(0)

while True:
    choice = int(input("\n1. Add an item\n2. Print currently added items\n3. Finished\n\nEnter your choice: "))

    if choice == 1:
        item, price, count = input("Enter an item: ").split()
        #shopping_list[item] = [int(price), int(count)]
        shopping_list.append(item)
        cost += float(price)*float(count)

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
        print(f'Total cost: {cost:.2f}')
        print("")
        break
    else:
        print("Error: Invalid choice, please try again.")