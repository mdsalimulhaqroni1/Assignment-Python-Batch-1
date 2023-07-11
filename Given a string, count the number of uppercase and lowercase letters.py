def count_letters(string):
    uppercase = 0
    lowercase = 0
    
    for char in string:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
            
    return uppercase, lowercase

string = input("Enter a string: ")

uppercase, lowercase = count_letters(string)

print(f"Number of uppercase letters: {uppercase}")  
print(f"Number of lowercase letters: {lowercase}")