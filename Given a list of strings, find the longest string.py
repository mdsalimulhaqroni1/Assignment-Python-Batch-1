def find_the_longest_string(list):
    longest_string = max(list, key=len)
    return longest_string

list = input("Enter the list of strings: ").split()
longest_string = find_the_longest_string(list)
print("The longest string is: ", longest_string)