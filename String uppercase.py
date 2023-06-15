def is_all_uppercase(s):
    return s.isupper()

input_string = input("Enter a String: ")
if is_all_uppercase(input_string):
    print("True")
else:
    print("False")