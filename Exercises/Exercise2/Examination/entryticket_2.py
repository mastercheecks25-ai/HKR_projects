shopping_list = []
title = input("Enter the title: ")

while True:
    choice = int(input("\n1. Add an item\n2. Print currently added items\n3. Finished\n\nEnter your choice: "))

    if choice == 1:
        item = input("Enter an item: ")
        shopping_list.append(item)
    elif choice == 2:
        print("Currently added items:")
        for i in shopping_list:
            print(f'{i}')
    elif choice == 3:
        dashes = len(title)
        # ----------If the padding has to be exact-------- #
        print(f"\n{'-' * dashes:-^{dashes + 6}}\n{title:^{dashes + 6}}\n{'-' * dashes:-^{dashes + 6}}")#
        for i in shopping_list:
            print(f'{i}')
        print("")
        break
    else:
        print("Error: Invalid choice, please try again.")