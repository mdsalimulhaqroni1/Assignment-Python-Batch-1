def count_words(string):
    words = string.split()
    return len(words)

strings = input("Enter a string: ").split()

for string in strings:
    words = count_words(string)
    print("Number of words in", string + ":", words)
    