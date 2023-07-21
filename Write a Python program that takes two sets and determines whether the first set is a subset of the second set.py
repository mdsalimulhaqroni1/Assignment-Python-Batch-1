def check_subset(set1, set2):
    if set1.issubset(set2):
        print("The first set is a subset of the second set")
    else:
        print("The first set is not a subset of the seecond set")

set1 = input("Enter the first set: ").split()
set1 = set(set1)

set2 = input("Enter the second set: ").split()
set2 = set(set2)

check_subset(set1, set2)