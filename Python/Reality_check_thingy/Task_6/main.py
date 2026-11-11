shopping_list = []
title = input("Enter the title: ")
edited = False

while True:
    choice = input("\n1. Add an item\n2. Print currently added items\n3. Finished\n\nEnter your choice: ")

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
        if edited:
            print(f"{'(edited)':^20}")
        print("-" * 20)

        for i in shopping_list:
            print(f'{i}')
        print("")
        break
    elif choice == 'C':
        #while True:
            new_title = input("Enter new title: ")
            if title == new_title:
                print("INFO: The new title is the same as the old one.")
            elif new_title == '':
                print("ERROR: Title can not be empty.")
            elif new_title == "Who is the best?":
                print("*" * 21)
                print(("* You are the best! *\n") * 10, end="")
                print("*" * 21, end="") 
            else:
                title = new_title
                edited = True
    else:
        print("Error: Invalid choice, please try again.")
    