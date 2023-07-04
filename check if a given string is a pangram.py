import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    sentence = sentence.lower()
    for char in sentence:
        if char.isalpha():
            alphabet.discard(char)
    return len(alphabet) == 0

sentence = input("Enter a sentence: ")
if is_pangram(sentence):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
