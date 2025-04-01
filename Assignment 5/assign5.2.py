numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))

result = numbers[0] == numbers[-1] if numbers else False

print(f"First and last number are the same: {result}")