def concatenate_strings(lst):
    result = ""
    for string in lst:
        result += string
    return result

lst = input("Enter a list of strings (space-separated): ").split()

result = concatenate_strings(lst)
print("Concatenated string:", result)
