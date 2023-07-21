def print_difference(set1, set2):
    difference_set = set.difference(set1, set2)
    print("The difference between the sets is:", difference_set)

set1 = input("Enter the first set:").split()
set1 = set(set1)

set2 = input("Enter the second set: ").split()
set2 = set(set2)

print_difference(set1, set2)