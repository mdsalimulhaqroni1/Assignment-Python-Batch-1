def remove_duplicates(lst):
    unique_lst = list(set(lst))
    return unique_lst

lst = input("Enter a list of tuples (space-separated): ").split()
lst = [tuple(map(int, tpl.split(','))) for tpl in lst]

unique_list = remove_duplicates(lst)
print("List of tuples after removing duplicates:", unique_list)
