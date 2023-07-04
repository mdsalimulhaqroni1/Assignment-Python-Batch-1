def find_max_min(numbers):
    return max(numbers), min(numbers)
numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
max_num, min_num = find_max_min(numbers)
print(f"The maximum number is {max_num} and the minimum number is {min_num}.")