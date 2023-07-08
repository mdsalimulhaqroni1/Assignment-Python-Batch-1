def is_perfect_square(number):
    if number  <0:
        return False
    else:
        sqrt = int(number ** 0.5)
        return sqrt * sqrt == number

number = int(input("Enter a number: "))
if is_perfect_square(number):
    print("The number is a perfect square.")
else:
    print("The number is not a perfect square.")
