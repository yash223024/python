def check_even_odd():
    num = int(input("Enter a number: "))

    if num == 0:
        print("The number is zero.")
    elif num % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")


if __name__ == "__main__":
    check_even_odd()