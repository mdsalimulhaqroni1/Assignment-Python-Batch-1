def getting_last_two_elements(list):
    return list[-2:]

list = input("Enter a list of elements: ").split()
last_two_elements = getting_last_two_elements(list)
print("First three elements", last_two_elements)