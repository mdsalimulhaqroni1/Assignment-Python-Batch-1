def check_same_length(str1, str2):
    if len(str1) == len (str2):
        return True
    else:
        return False
    
str1 = input("Enter a first string: ")
str2 = input('Enter asecond string: ')

result = check_same_length(str1, str2)
print(result)
