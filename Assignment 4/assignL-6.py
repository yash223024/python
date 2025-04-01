num = int(input("Enter a number: "))


total = 0

print('"', end="")
for i in range(1, num + 1):
    total += i
    if i < num:
        print(i, end="+")
    else:
        print(i, end="=")
print(total, '"')