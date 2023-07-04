def sum_of_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum

number = int(input("Enter a number: "))
digit_sum = sum_of_digits(number)
print("Sum of digits:", digit_sum)