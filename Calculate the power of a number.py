def calculate_power(base, exponent):
    result = base ** exponent
    return result

base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
power = calculate_power(base, exponent)
print("The result is: ", power)