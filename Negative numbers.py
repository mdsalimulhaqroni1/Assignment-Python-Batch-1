def has_negative(numbers):
    for num in numbers:
        if num < 0 :
            return True
        return False
    
input_list = list(map(int, input("Enter a list of numbers: ").split()))
if has_negative(input_list):
    print("True")
else:
    print('False')