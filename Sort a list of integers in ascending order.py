def sort_list(list):
    sorted_list = sorted(list)
    return sorted_list

list = input("Enter a list of integers: ").split()
list = [int(num) for num in list]

sorted = sort_list(list)
print("Sorted list: ", sorted)
