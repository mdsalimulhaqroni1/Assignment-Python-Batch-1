def count_occurrences(lst, element):
    count = lst.count(element)
    return count

lst = input("Enter a list of elements (space-separated): ").split()
element = input("Enter the element to count: ")

occurrences = count_occurrences(lst, element)
print("Number of occurrences:", occurrences)
