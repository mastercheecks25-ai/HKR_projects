def print_menu():
    print("--------- Menu ----------")
    print("a) Add a new test subject")
    print("s) Show all information")
    print("r) Read from file")
    print("w) Write to file")
    print("q) Quit")
    print("-------------------------")


def new_test_subject():
    number = read_string("Number : ", 1, 99)
    time = read_int("Time   : ")
    return(number, time)


def write_data(test_subjects, filename):
    file = open(filename, "w")
    for i in test_subjects:
        file.write(f"{i[0]}\n{i[1]}\n")


def read_data(filename):
    file = open(filename, "r")
    test_subjects = []
    number_warn = []
    time_warn = []
    both_warn = []
    while True:
        number = file.readline().strip()
        if number == "":
            break
        time = file.readline().strip()
        one_subject = (number, int(time))
        if (int(number) > 99 or int(number) < 1) and (int(time) < 1 or int(time) > 60):
            both_warn.append(one_subject)
        elif int(number) > 99 or int(number) < 1:
            number_warn.append(one_subject)
        elif int(time) < 1 or int(time) > 60:
            time_warn.append(one_subject)
        
        test_subjects.append(one_subject)

    if number_warn != []:
        print("WARNING (number outside valid range):")
        for i in number_warn:
            print(f"Number {i[0]}, time {i[1]} minutes")
    if time_warn != []:
        print("\nWARNING (time outside valid range):")
        for i in time_warn:
            print(f"Number {i[0]}, time {i[1]} minutes")
    if both_warn != []:
        print("\nWARNING (both outside valid ranges):")
        for i in both_warn:
            print(f"Number {i[0]}, time {i[1]} minutes")

    return(test_subjects)


def print_test_subjects(test_subjects):
    print("---- Registered test subjects ----")
    for i in test_subjects:
        print(f"Number :{i[0]:>5}")
        print(f"Time   :{i[1]:>5}")
        print("")

def read_int(prompt):
    while True:
        try:
            number = int(input(prompt))
            return number
        except ValueError:
            print("ERROR: Please enter an integer number.")

def read_string(prompt, lower, upper):
    while True:
        number = int(input(prompt))
        if number >= lower and number <= upper:
            return str(number)
        else:
            print(f"ERROR: Number must be between {lower} and {upper}. Try again!")


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
        


if __name__ == '__main__':
    main()