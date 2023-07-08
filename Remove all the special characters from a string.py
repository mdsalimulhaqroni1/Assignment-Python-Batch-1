import re
def remove_special_characters(string):
    pattern = r'[^a-zA-Z0-9\s]'
    cleaned_string = re.sub(pattern, '', string)
    return cleaned_string

string = input("Enter a string: ")
cleaned_string = remove_special_characters(string)
print("The cleaned string is: ", cleaned_string)