def getting_first_three_elements(list):
    return list[:3]

list = input("Enter a list of elements: ").split()
first_three_elements = getting_first_three_elements(list)
print("First three elements", first_three_elements)