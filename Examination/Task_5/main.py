shopping_list = []
title = input("Enter the title: ")
tot = 0
min = 1000000000
max = 0
cost = 0


while True:
    choice = input("\n1. Add an item\n2. Print currently added items\n3. Finished\nC. Calculate price\n\nEnter your choice: ")

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
        print("")
        break
    elif choice == 'C':
        for i in range(3):
            while True:
                cost = int(input("What is the price: "))
                if cost < 0:
                    print("ERROR: Prices must be positive numbers. Try again!")
                else:
                    break
            if min > cost:
                min = cost
            if max < cost:
                max = cost
            tot +=  cost
        print (f" Total price:{tot:>5} SEK")
        print (f"Min: {min}, Max: {max}, Average: {(tot/3):.2f}")
    else:
        print("Error: Invalid choice, please try again.")