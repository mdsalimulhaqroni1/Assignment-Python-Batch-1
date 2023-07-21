def merge_tuple(tuple1, tuple2):
    return tuple1 + tuple2

tuple1 = input("Enter the first tuple: ").split(",")
tuple1 = tuple(tuple1)

tuple2 = input("Enter the second tuple ").split(",")
tuple2 = tuple(tuple2)

merged_tuple = merge_tuple(tuple1, tuple2)
print("The merged tuple is: ", merged_tuple)
