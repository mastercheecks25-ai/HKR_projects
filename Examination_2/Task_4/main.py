def print_menu():
    print("--------- Menu ----------")
    print("a) Add a new test subject")
    print("s) Show all information")
    print("r) Read from file")
    print("w) Write to file")
    print("q) Quit")
    print("T) Find time in file")
    print("-------------------------")


def new_test_subject():
    number = input("Enter subject number: ")
    time = int(input("Enter lap time in minutes: "))
    return(number, time)


def write_data(test_subjects, filename):
    file = open(filename, "w")
    for i in test_subjects:
        file.write(f"{i[0]}\n{i[1]}\n")


def read_data(filename):
    file = open(filename, "r")
    test_subjects = []
    while True:
        number = file.readline().strip()
        if number == "":
            break
        time = file.readline().strip()
        one_subject = (number, int(time))
        test_subjects.append(one_subject)
    return(test_subjects)


def print_test_subjects(test_subjects):
    print("---- Registered test subjects ----")
    for i in test_subjects:
        print(f"Number :{i[0]:>5}")
        print(f"Time   :{i[1]:>5}")
        print("")


def main():
    test_subjects = []
    while True:
        print_menu()
        choice = input("Your Choice: ")
        if choice == "a":
            test_subjects.append(new_test_subject())
        elif choice == "s":
            print_test_subjects(test_subjects)
        elif choice == "r":
            filename = input("Filename: ")
            test_subjects = read_data(filename)
        elif choice == "w":
            filename = input("Filename: ")
            write_data(test_subjects, filename)
            print("\n *** Data written to file ***\n")
        elif choice == 'q':
            break
        elif choice == "T":
            while True:
                try:
                    filename = input("Filename: ")
                    number = input("number: ")
                    test_subjects = read_data(filename)
                    time = 0
                    smth = False
                    for i in test_subjects:
                        if i[0] == number:
                            time = i[1]
                            print(f"Test subject {i[0]} ran around the lake in {i[1]} minutes.")
                            smth = True
                    if not smth:
                        print("INFO: No test subject with that number was found.")
                        bre
                    slower = 100000000000
                    faster = 0
                    slower_num = ''
                    faster_num = ''

                    for j in test_subjects:
                        if j[1] < time and j[1] > faster:
                            faster = j[1]
                            faster_num = j[0]

                        if j[1] > time and j[1] < slower:
                            slower = j[1]
                            slower_num = j[0]
                    print(f"Closest faster: Test subject {faster_num:>3} with {faster} minutes.")
                    print(f"Closest slower: Test subject {slower_num:>3} with {slower} minutes.")
                    break
                except:
                    print("ERROR: The specified file was not found. Please try again.")


        


if __name__ == '__main__':
    main()