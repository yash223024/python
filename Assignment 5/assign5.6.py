
my_tuple = (10, 20, 30, 40, 50)

element = int(input("Enter an element to check: "))


if element in my_tuple:
    print(f"{element} exists in the tuple.")
else:
    print(f"{element} does not exist in the tuple.")