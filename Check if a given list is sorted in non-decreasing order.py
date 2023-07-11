def is_sorted(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            return False
    return True

lst = input("Enter a list of numbers (space-separated): ").split() 
lst = [int(num) for num in lst]

if is_sorted(lst):
    print("The list is sorted in non-decreasing order.")
else: 
    print("The list is not sorted in non-decreasing order.")
