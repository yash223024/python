def find_greatest():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    greatest = max(num1, num2, num3)

    print(f"The greatest number is: {greatest}")


if __name__ == "__main__":
    find_greatest()