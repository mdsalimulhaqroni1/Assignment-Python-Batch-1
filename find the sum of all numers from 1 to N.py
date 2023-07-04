def sum_of_n(n):
    return n*(n+1)//2
N = int(input("Enter a number: "))
sum = sum_of_n(N)
print(f"The sum of all numbers from 1 to {N} is {sum}.")