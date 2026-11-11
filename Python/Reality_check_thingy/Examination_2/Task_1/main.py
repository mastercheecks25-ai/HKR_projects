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
    try:
        file = open(filename, "r")
        test_subjects = []
        num_test_subjects = 0
        while True:
            number = file.readline().strip()
            if number == "":
                break
            num_test_subjects += 1
            time = file.readline().strip()
            one_subject = (number, int(time))
            test_subjects.append(one_subject)
        print("*** Data read from file ***")
        print(f"*** {num_test_subjects} test subjects found ***")
        return(test_subjects)
    except:
        print("*** ERROR: The specified file could not be read. ***")

def load_range(filename, start, stop):
    try:
        file = open(filename, "r")
        test_subjects = []
        num_test_subjects = 0
        while True:
            number = file.readline().strip()
            if number == "":
                break
            num_test_subjects += 1
            time = file.readline().strip()
            one_subject = (number, int(time))
            if int(number) <= int(stop) and int(number) >= int(start):
                test_subjects.append(one_subject)
        print("*** Data read from file ***")
        print(f"*** {num_test_subjects} test subjects found ***")
        return(test_subjects)
    except:
        print("*** ERROR: The specified file could not be read. ***")



def print_test_subjects(test_subjects):
    print("---- Registered test subjects ----")
    if test_subjects == []:
        print("No test subjects found")
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
        elif choice == "L":
            filename = input("Filename: ")
            start = input("start: ")
            stop = input("stop: ")
            test_subjects = load_range(filename, start, stop)
        elif choice == 'q':
            break
        


if __name__ == '__main__':
    main()