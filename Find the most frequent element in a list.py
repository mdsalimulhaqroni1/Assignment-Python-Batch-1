from collections import Counter

def find_most_frequent(list):
    counter = Counter(list)
    most_frequent = counter.most_common(1)[0][0]
    return most_frequent

list = input("Enter a list of elements: ").split()

most_frequent_element = find_most_frequent(list)
print("Most frequent element:", most_frequent_element)
