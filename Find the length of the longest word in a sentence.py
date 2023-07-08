def find_longest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)
    return len(longest_word)

sentence = input("Enter a sentence: ")
length = find_longest_word(sentence)
print("Length of the longest word:", length)
