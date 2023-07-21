def print_intersection(set1, set2):
    intersection_set = set1.intersection(set2)
    print("The intersection of the sets is:", intersection_set)

set1 = input("Enter the first set: ").split()
set1 = set(set1)

set2 = input("Enter the second set: ").split()
set2 = set(set2)

print_intersection(set1, set2)