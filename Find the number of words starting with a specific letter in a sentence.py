def count_words_starting_with_letter(sentence, letter):
    words = sentence.split()
    count = 0
    for word in words:
        if word.lower().startswith(letter.lower()):
            count += 1
    return count

sentence = input("Enter a sentence: ")
letter = input("Enter a letter: ")

word_count = count_words_starting_with_letter(sentence, letter)
print("Number of words starting with", letter + ":", word_count)
