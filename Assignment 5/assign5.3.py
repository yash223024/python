numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

divisible_by_5 = [num for num in numbers if num % 5 == 0]


print(f"Numbers divisible by 5: {divisible_by_5}")