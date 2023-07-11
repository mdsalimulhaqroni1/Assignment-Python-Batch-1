def find_third_largest(lst):
    if len(lst) < 3:
        return "List should have at least three elements."
    lst = sorted(lst, reverse=True)
    return lst[2]

lst = input("Enter a list of integers (space-separated): ").split()
lst = [int(num) for num in lst]  # Convert input strings to integers

third_largest = find_third_largest(lst)
print("Third largest element:", third_largest)
