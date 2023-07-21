def print_union(set1, set2):
    union_set = set1.union(set2)
    print("The union of the sets is:", union_set)

set1 = input("Enter the first set: ").split()
set1 = set(set1)

set2 = input("Enter the second set: ").split()
set2 = set(set2)

print_union(set1, set2)