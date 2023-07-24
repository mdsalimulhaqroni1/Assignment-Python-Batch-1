my_dict = {}
friend1_name = input("Enter your friend1 name: ")
friend1_age = int(input("Enter your friend1 age: "))

friend2_name = input("Enter your friend2 name: ")
friend2_age = int(input("Enter your friend2 age: "))

friend3_name = input("Enter your friend3 name: ")
friend3_age = int(input("Enter your friend3 age: "))

my_dict[friend1_name] = friend1_age
my_dict[friend2_name] = friend2_age
my_dict[friend3_name] = friend3_age

print("Dictionary with key-value pairs created: ", my_dict)