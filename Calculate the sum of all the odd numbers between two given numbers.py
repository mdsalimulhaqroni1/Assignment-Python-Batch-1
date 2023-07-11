def sum_of_odd_numbers(start, end):
    sum = 0
    for num in range(start, end+1):
        if num % 2 != 0:
            sum += num
    return sum

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

sum_of_odds = sum_of_odd_numbers(start, end)
print("Sum of odd numbers:", sum_of_odds)
