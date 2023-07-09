def check_unique(list):
    if len(list) == len(set(list)):
        return True
    else:
        return False
    
list = input("Enter a list of numbers: ").split()

if check_unique(list):
    print("All elements are unique")
else:
    print("List has duplicates")