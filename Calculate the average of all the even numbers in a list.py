def calculate_average(lst):
    even_numbers = [num for num in lst if num % 2 == 0]
    if len(even_numbers) == 0:
        return "No even numbers in the list."
    else:
        average = sum(even_numbers) / len(even_numbers)
        return average

lst =input("Ebnter a list of numbers separated by space:").split()
lst = [int(num) for num in lst]  # Convert input strings to integers

average = calculate_average(lst)
print("Average of even numbers:", average)
