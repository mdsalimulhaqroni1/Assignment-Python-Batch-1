def getting_first_two_elements(list):
    return list[:2]

list = input("Enter a list of elements: ").split()
first_two_elements = getting_first_two_elements(list)
print("First two elements", first_two_elements)