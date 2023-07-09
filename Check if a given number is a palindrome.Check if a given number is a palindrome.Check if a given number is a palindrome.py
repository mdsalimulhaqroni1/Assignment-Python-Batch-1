def is_palindrome(number):
    orginal_number = number
    reverse_number = 0
    while number > 0:
        digit = number % 10
        reverse_number = reverse_number * 10 + digit
        number = number // 10
    return orginal_number == reverse_number

number = int(input("Enter a number: "))
if is_palindrome(number):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")