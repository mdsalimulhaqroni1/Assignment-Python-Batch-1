def is_palindrome(string):
    string = string.lower()  # Convert string to lowercase-insensitive comparison
    reversed_string = string[::-1]  # Reverse the string using slicing
    if string == reversed_string:
        return True
    else:
        return False

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")