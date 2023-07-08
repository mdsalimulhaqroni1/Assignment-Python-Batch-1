def reverse_string(string):
    return string[::-1]

string = input("Enter a string: ")
string_reversed = reverse_string(string)
print("The reversed string is: ", string_reversed)