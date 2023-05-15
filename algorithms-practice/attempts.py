def multiples_3_5(number = 1000):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum



def fibonacci():
    sum = 0
    prev = 1 
    curr = 2
    while curr <= 4000000:
        if curr % 2 == 0:
            sum += curr
        prev = curr
        curr = prev + curr
    return sum



def largest_prime_factor(number = 600851475143 ):
    i = 2
    while i * i < number:
        while number % i == 0:
            number = number / i
        i = i + 1
    return number


def largest_palendrome_product():
    palindrome = 0 
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = j * i 
            if str(product) == str(product)[::-1] and product > palindrome:
                palindrome = product
    return palindrome

print(largest_palendrome_product())