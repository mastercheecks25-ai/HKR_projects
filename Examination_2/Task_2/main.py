def print_menu():
    print("--------- Menu ----------")
    print("a) Add a new test subject")
    print("s) Show all information")
    print("r) Read from file")
    print("w) Write to file")
    print("q) Quit")
    print("T) Statistics")
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

def statistics(filename):
    file = open(filename, "r")
    test_subjects = []
    num = 0
    sum = 0
    while True:
        number = file.readline().strip()
        if number == "":
            break
        time = file.readline().strip()
        sum += int(time)
        num += 1
        one_subject = (number, int(time))
        test_subjects.append(one_subject)
    avg = float(sum)/float(num)
    return(test_subjects, avg)

def min_and_max(test_subjects):
    max = 0
    min = 100000000000000
    for i in test_subjects:
        if i[1] > max:
            max = i[1]
        if i[1] < min:
            min = i[1]
    return(min, max)

def division_groups(test_subjects):
    group1 = []
    group2 = []
    group3 = []
    for i in test_subjects:
        if i[1] <= 10:
            group1.append(i[1])
        if i[1] > 10 and i[1] <= 20:
            group2.append(i[1])
        if i[1] > 20:
            group3.append(i[1])
    gup1perc = float((len(group1)/len(test_subjects)) * 100)
    gup2perc = float((len(group2)/len(test_subjects)) * 100)
    gup3perc = float((len(group3)/len(test_subjects)) * 100)
    len_group1 = len(group1)
    len_group2 = len(group2)
    len_group3 = len(group3)
    return [(len_group1, gup1perc), (len_group2, gup2perc), (len_group3, gup3perc)]
    

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
            filename = input("Filename: ")
            avg_test = statistics(filename)
            print(f"Average lap time: {avg_test[1]:.1f} minutes")
            test_subjects = avg_test[0]
            max_and_min = min_and_max(test_subjects)
            print(f'(Min: {max_and_min[0]} minutes, Max: {max_and_min[1]} minutes)')
            group1 = division_groups(test_subjects)[0]
            group2 = division_groups(test_subjects)[1]
            group3 = division_groups(test_subjects)[2]
            print(f"(Group 1: {group1[1]:.1f}% ({group1[0]}), Group 2: {group2[1]:.1f}% ({group2[0]}), Group 3: {group3[1]:.1f}% ({group3[0]}))")



if __name__ == '__main__':
    main()