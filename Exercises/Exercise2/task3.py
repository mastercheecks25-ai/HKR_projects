num = str(input("Enter a number: "))
sum = 0
for i in range(len(num)):
    sum += int(num[i])
print(16*sum)