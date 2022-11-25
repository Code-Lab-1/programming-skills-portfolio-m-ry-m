#Calculate the sum of all numbers from 1 to a given number
j = 0
n = int(input("Enter number "))
for i in range(1, n + 1, 1):
    j += i
print("\n")
print("Sum is: ", j)