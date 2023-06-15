def avg_of_three_numbers(a,b,c):
    return(a+b+c)/3

num1 = float(input("Enter first numbers"))
num2 = float(input("Enter second number"))
num3 = float(input('Enter thrid number'))

avg = avg_of_three_numbers(num1, num2, num3)

print("The avg of {}, {} and {} is {}".format(num1, num2, num3, avg))