def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    return list(common_elements)

list1 = input("Enter list 1: "). split()
list2 = input("Enter list 2: ").split()

common_elements = find_common_elements(list1, list2)
print("Common elements: ", common_elements)