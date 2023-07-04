def reverse_list(lst):
    reversed_lst = lst[::-1]  # Reverse the list using slicing
    return reversed_lst

lst = input("Enter a list of integers (space-separated): ").split()
lst = [int(num) for num lst]  # Convert input strings to integers
reversed_lst = reverse_list(lst)
print("Reversed list:", reversed_lst)
