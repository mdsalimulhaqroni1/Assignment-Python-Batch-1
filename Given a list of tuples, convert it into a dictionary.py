def convert_to_dict(lst):
    dictionary = dict(lst)
    return dictionary

lst = input("Enter a list of tuples (space-separated): ").split()
lst = [tuple(map(int, tpl.split(','))) for tpl in lst]

dictionary = convert_to_dict(lst)
print("Dictionary:", dictionary)