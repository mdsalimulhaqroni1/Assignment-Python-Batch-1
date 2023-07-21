def get_element_at_index_2(tuple):
    return tuple[2]

tuple1 = input("Enter a tuple of elements: ").split(",")
tuple1 = tuple(tuple1)

elements_at_index_2 = get_element_at_index_2(tuple1)
print("Element at index 2:", elements_at_index_2)


