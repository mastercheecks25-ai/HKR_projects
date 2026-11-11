choice = int(input("----Menu----\n1. Calculate n raised to the power of n\n2. Calculate the sum of the arithmetic series 1, 2, 3, ..., n\n: "))
n = int(input("Enter a number: "))
if choice == 1:
    print(n**n)
elif choice == 2:
    sum = 0
    for i in range(n + 1):
        sum += i
    print (sum)