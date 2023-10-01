"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError

    list = []
    num = 2
    while len(list) < number_of_primes:
        if isPrime(num):
            list.append(num)
        num += 1
    return list

def isPrime(n):
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
