def reverse_list(list):
    return list[::-1]

list = input("Enter a list of elements:").split()
reversed_list = reverse_list(list)
print("Reversed list:", reversed_list)