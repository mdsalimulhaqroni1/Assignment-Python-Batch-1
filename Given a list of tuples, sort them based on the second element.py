def sort_tuples(list):
    sorted_list = sorted(list, key = lambda x: x[1])
    return sorted_list

list = input("Enter a list of tuples: ").split()
list = [tuple(map(int, tpl.split(','))) for tpl in list]

sorted_list = sort_tuples(list)
print("Sorted list of tuples: ", sorted_list)
