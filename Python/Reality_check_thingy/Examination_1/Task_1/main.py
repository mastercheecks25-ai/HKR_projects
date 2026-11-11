shopping_list = []
title = input("Enter the title: ")
cost = float(0)
price_low = 10000
price_High = 0
avg = 0
units = 0
prices = []

while True:
    choice = int(input("\n1. Add an item\n2. Print currently added items\n3. Finished\n\nEnter your choice: "))

    if choice == 1:
        item = input("Enter an item: ")
        #--------------------------------------- 3rd grade -----------------------------------#
        price = float(input("Enter the price:"))
        count = float(input("Enter the count:"))
        shopping_list.append(item)
        cost += float(price) * float(count)

        #-------------------------------------------------------------------------------------#
        #--------------------------------------- 4th grade -----------------------------------#
        units += int(count)
        #-------------------------------------------------------------------------------------#
        print("sum rn", sum)
        if price < price_low:
            price_low = price
        if price > price_High:
            price_High = price
        

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
        print(f'Total cost: {cost:.2f} SEK')
        print(f"{"units":<10}: {units}")
        print(f"Price info: {price_low:.2f} (Low) / {price_High:.2f} (High) / {(cost/units):.2f} (Average) SEK")
        print("")
        break
    else:
        print("Error: Invalid choice, please try again.")