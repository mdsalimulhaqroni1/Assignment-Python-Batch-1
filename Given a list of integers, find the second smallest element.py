def find_second_smallest(list):
    smallest = float('inf')
    second_smallest = float('inf')
    for i in list:
        if i < smallest:
            second_smallest = smallest
            smallest = i
        elif i < second_smallest and i != smallest:
            second_smallest = i
    return second_smallest

list = input("Enter a list of integers: ").split()
list = [int(i) for i in list]  # Convert input strings to integers

second_smallest = find_second_smallest(list)
print("Second smallest element:", second_smallest)
