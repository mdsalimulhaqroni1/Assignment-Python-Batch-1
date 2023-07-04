def check_equal(lst1, lst2):
    if lst1 == lst2:
        return True
    else:
        return False

lst1 = input("Enter elements of the first list (space-separated): ").split()
lst1 = [int(num) for num in lst1]  # Convert input strings to integers

lst2 = input("Enter elements of the second list (space-separated): ").split()
lst2 = [int(num) for num in lst2]  # Convert input strings to integers

if check_equal(lst1, lst2):
    print("The lists are equal.")
else:
    print("The lists are not equal.")
