def check_number():
    num = float(input("Enter a number: "))

    if num > 0:
        print("The number is positive.")
    elif num < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")


if __name__ == "__main__":
    check_number()