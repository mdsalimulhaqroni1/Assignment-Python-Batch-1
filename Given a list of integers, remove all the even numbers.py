def remove_even_numbers(lst):
    return [num for num in lst if num % 2 != 0]

lst = input("Enter a list of integers (space-separated): ").split()
lst = [int(num) for num in lst]  # Convert input strings to integers

lst = remove_even_numbers(lst)
print("List after removing even numbers:", lst)
