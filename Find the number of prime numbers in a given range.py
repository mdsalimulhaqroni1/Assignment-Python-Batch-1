def count_prime(start, end):
    count = 0
    for i in range(start, end + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1 ):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count

start = int(input("Enter the start number: "))
end = int(input("Enter the ending number: "))

prime_count = count_prime(start, end)
print("Number of prime numbers between", start, "and", end, ":", prime_count)


