def count_vowels(string):
    vowel = "aeIOU"
    count = 0
    for char in string:
        if char in vowel:
            count += 1
            return count
        
string = input("Enter a String: ")
num_vowels = count_vowels(string)
print("Number of vowels in the string:", num_vowels)