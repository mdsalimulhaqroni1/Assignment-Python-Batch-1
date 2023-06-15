def add_numbers(a, b):
    return a+b

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

sum = add_numbers(num1,num2)
print("The sum of {} and {} is: {}".format(num1, num2, sum))