def find_average(lst):
    if len(lst) == 0:
        return "List is empty."
    total = sum(lst)
    average = total / len(lst)
    return average

lst = input("Enter a list of integers (space-separated): ").split()
lst = [int(num) for num in lst]  # Convert input strings to integers
average = find_average(lst)
print("Average:", average)
