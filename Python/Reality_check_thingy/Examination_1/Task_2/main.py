shopping_list = []
title = input("Enter the title: ")
items = 0

while True:
    choice = str(input("\n1. Add an item\n2. Print currently added items\n3. Finished\n\nEnter your choice: "))

    if choice == "1":
        #--------------------------------------------grade 4--------------------------------------#
        if items > 9:
            print("ERROR: The list is full, your item was not added")
        #-------------------------------------------------------------------------------------------#
        else:
            item = input("Enter an item: ")
            shopping_list.append(item)
            items += 1

    elif choice == "2":
        print("Currently added items:")
        for i in shopping_list:
            print(f'{i}')
        
    #--------------------------------------------grade 3------------------------------------------------#
    elif choice == "S":
        print (f"Currently the list contains {items} item(s)")
        #------------------------------------------grade 5-----------------------#
        print(f'[{("*"*items):<10}]')
        #------------------------------------------------------------------------#
    #---------------------------------------------------------------------------------------------------#

    elif choice == "3":
        print("-" * 20)
        print(f"{title:^20}")
        print("-" * 20)

        for i in shopping_list:
            print(f'{i}')
        print("")
        break
    else:
        print("Error: Invalid choice, please try again.")