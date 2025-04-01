numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))


if len(numbers) > 4:

    element = numbers.pop(4)


    numbers.insert(2, element)


    numbers.append(element)


    print(f"Updated list: {numbers}")
else:
    print("The list must contain at least 5 elements.")