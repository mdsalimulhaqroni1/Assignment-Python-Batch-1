def find_median(list):
    sorted_list = sorted(list)
    n = len(sorted_list)
    if n % 2 == 0:
        median = (sorted_list[n//2 - 1] + sorted_list[n//2 ]) / 2
    else:
        median = sorted_list[n // 2]
    return median

list = input("Enter a list of ingergers: ").split()
list = [int(n) for n in list]
median = find_median(list)
print("The median is: ", median)


