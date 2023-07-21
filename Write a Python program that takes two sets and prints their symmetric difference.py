'''
def symetric_difference(set1, set2):
    symetric_difference = set1.symetric_difference(set2)
    print("The symetric difference of the two sets is: ", symetric_difference)

set1 = input("Enter the first set: ").split()
set1 = set(set1)

set2 = input("Enter the second set: ").split()
set2 = set(set2)

symetric_difference(set1, set2)
'''

def print_symmetric_difference(set1, set2):
    symmetric_difference_set = set1.symmetric_difference(set2)
    print("Symmetric difference of the two sets:", symmetric_difference_set)

set1 = input("Enter the first set of elements (space-separated): ").split()
set1 = set(set1)

set2 = input("Enter the second set of elements (space-separated): ").split()
set2 = set(set2)

print_symmetric_difference(set1, set2)
