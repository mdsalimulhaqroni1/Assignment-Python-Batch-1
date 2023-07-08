def is_anagram(list1, list2):
    list1 = list1.lower()
    list2 = list2.lower()
    return sorted(list1) == sorted(list2)

list1 = input("Enter the first string: ")
list2 = input("Enter the second string: ")

if is_anagram(list1, list2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")