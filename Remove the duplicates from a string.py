def remove_duplicates(string):
    unique_chars = []
    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)

string =input("Enter a string: ")
result = remove_duplicates(string)
print("String after removing duplicates:", result)