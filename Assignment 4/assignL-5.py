# Get user input
num = int(input("Enter a number: "))

factorial = 1


for i in range(1, num + 1):
    factorial *= i

print(f"{num}! =", end=" ")
for i in range(1, num + 1):
    if i < num:
        print(i, end=" * ")
    else:
        print(i, "=", factorial)