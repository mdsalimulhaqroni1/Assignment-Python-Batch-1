def is_even(number):
    return number % 2 == 0

num = int(input("Enter a number: "))
if is_even(num):
    print("True")
else:
    print("False")