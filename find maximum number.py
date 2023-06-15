def find_max(a,b,c):
    if a>=b and a>= c:
        return a
    elif b>= a and b>= c:
        return b
    else:
        return c
    
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))
max_number = find_max(num1, num2, num3)

print(f"The maximum number among {num1}, {num2}, and {num3} is max number {max_number}.")