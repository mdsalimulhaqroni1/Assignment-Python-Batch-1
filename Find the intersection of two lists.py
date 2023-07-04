def find_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

lst1 = input("Enter elements of the first list (space-separated): ").split()
lst1 = [int(num) for num in lst1]  # Convert input strings to integers

lst2 = input("Enter elements of the second list (space-separated): ").split()
lst2 = [int(num) for num in lst2]  # Convert input strings to integers

intersection = find_intersection(lst1, lst2)
print("Intersection of the two lists:", intersection)
