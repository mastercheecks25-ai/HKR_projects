def print_menu():
    print("--------- Menu ----------")
    print("a) Add a new test subject")
    print("s) Show all information")
    print("r) Read from file")
    print("w) Write to file")
    print("q) Quit")
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

def replay_from_file(history):
    file = open("session_log.txt", "r")
    commands = file.readlines()
    file.close()

    test_subjects = []

    for line in commands:
        prts = line.strip().split(";")
        choice = prts[0]

        if choice == "a":
            test_subjects.append((prts[1], int(prts[2])))
        elif choice == "s":
            print_test_subjects(test_subjects)
        elif choice == "w":
            filename = prts[1]
            write_data(test_subjects, filename)
            print("\n *** Data written to file ***\n")
        elif choice == "r":
            filename = prts[1]
            test_subjects = read_data(filename)
            print("*** Data read from file ***")
        elif choice == "H":
            print("History\n-------")
            for i in history:
                print(i)
    return(test_subjects)
        
        
        


def main():
    test_subjects = []
    history = []
    while True:
        print_menu()
        choice = input("Your Choice: ")
        if choice == "a":
            smth = new_test_subject()
            test_subjects.append(smth)
            history.append("a")
            file = open("session_log.txt", "a+")
            file.write(f"a;{smth[0]};{smth[1]}\n")
            file.close()
        elif choice == "s":
            print_test_subjects(test_subjects)
            history.append("s")
            file = open("session_log.txt", "a+")
            file.write("s\n")
            file.close()
        elif choice == "r":
            filename = input("Filename: ")
            test_subjects = read_data(filename)
            history.append("r")
            file = open("session_log.txt", "a+")
            file.write(f"r;{filename}\n")
            file.close()
        elif choice == "w":
            filename = input("Filename: ")
            write_data(test_subjects, filename)
            print("\n *** Data written to file ***\n")
            history.append(f"w")
            file = open("session_log.txt", "a+")
            file.write(f"w;{filename}\n")
            file.close()
        elif choice == 'q':
            break
        elif choice == "H":
            print("History\n-------")
            history.append("H")
            for i in history:
                print(i)
            file = open("session_log.txt", "a+")
            file.write("H\n")
            file.close()
        elif choice == "F":
            history.append("F")
            test_subjects = replay_from_file(history)
            
        

        


if __name__ == '__main__':
    main()