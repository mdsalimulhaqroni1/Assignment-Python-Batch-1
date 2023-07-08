def sum_of_even_numbers(start, end):
    sum = 0
    for i in range(start, end + 1):
        if i % 2 == 0:
            sum += i
    return sum

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

sum = sum_of_even_numbers(start, end)
print("The sum of even numbers: ", sum)