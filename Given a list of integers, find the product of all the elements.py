def find_product(lst):
    product = 1
    for num in lst:
        product *= num
    return product

lst = input("Enter a list of integers (space-separated): ").split()
lst = [int(num) for num in lst] # convert to integers

product = find_product(lst)
print("Product of all elements:", product)