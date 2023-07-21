def unpack_tuple(tuple1):
    return tuple1

tuple1 = input("Enter the tuple: ").split(",")
tuple1 = tuple(tuple1)

var1, var2, var3 = unpack_tuple(tuple1)

print("The unpacked veriables are: " )
print("Variable 1:", var1)
print("Variable 2:", var2)
print("variable 3:", var2)
