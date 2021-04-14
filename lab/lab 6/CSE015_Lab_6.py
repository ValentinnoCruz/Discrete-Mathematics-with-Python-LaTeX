# CSE 015 Discrete Mathematics
# Lab Assignment 6
# Mathematical functions that may be of use
from math import sqrt
from math import ceil


# Exercise 1. Implement the algorithm covered in lectures that determines if an integer n is prime. Your function should return True, if n is prime, and False otherwise. Your algorithm has to be effective for n ~ 1,000,000,000,000.
def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True

    for i in range(2, ceil(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


# Exercise 2. Using the isPrime function above, implement a function that takes in an integer n, and returns the smallest prime number greater than n. Your code should computer in a reasonable time for n ~ 1,000,000,000,000.
def nextPrime(n):
    # Provide a correct implementation for this function

    if (n <= 1):
        return 2

    prime = n
    check = False

    while (not check):
        prime = prime + 1

        if (isPrime(prime) == True):
            check = True

    return prime


# Exercise 3. It is sometimes necessary to find all prime numbers less than some integer n. Implement a function that takes in an integer n and returns a list of all primes that are less than or equal to n. Your algorithm should be effective for n ~ 1,000,000
def allPrimes(n):
    # Provide a correct implementation for this function
    primes = []
    for i in range(n):
        if isPrime(i):
            primes.append(i)
    return primes


# Exercsie 4. The Fundamental Theorem of Arithmetic tells us that every positive integer n, can be expressed uniquely as a product of primes in non-decreasing order. Implement the method covered in class (and not any other method), for finding prime factorizations of integers. The function below should take in an integer n, and return a list of the prime factors of n.
def factorize(n):
    # Provide a correct implementation for this function
    if n == 1:
        return []
    elif isPrime(n):
        return [n]
    else:
        for i in range(2, ceil(sqrt(n) + 1)):
            if n % i == 0:
                return [i] + factorize(n / i)


# TEST SUITE

# A simple comparison
def check(a, b):
    if a == b:
        print("PASSED")

    else:
        print("FAILED")


# Check to see if some numbers are prime
result1 = isPrime(7)
expected1 = True
print("7 is prime:\t\t\t\t", result1)
check(result1, expected1)

result2 = isPrime(15)
expected2 = False
print("15 is prime:\t\t\t\t", result2)
check(result2, expected2)

result3 = isPrime(1000000)
expected3 = False
print("1,000,000 is prime:\t\t\t", result3)
check(result3, expected3)

result4 = isPrime(1000003)
expected4 = True
print("1,000,003 is prime:\t\t\t", result4)
check(result4, expected4)

result5 = isPrime(999999999989)
expected5 = True
print("999,999,999,989 is prime:\t\t", result5)
check(result5, expected5)

print("Overall isPrime functionality")
check([result1, result2, result3, result4, result5], [True, False, False, True, True])

# Print the first 20 primes
k = 0
result = []
expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
for i in range(20):
    k = nextPrime(k)
    result.append(k)
print("The first 20 primes:\t\t\t", result)
check(result, expected)

# Generate all primes
result = allPrimes(20)
expected = [2, 3, 5, 7, 11, 13, 17, 19]
print("All primes less than 20:\t\t", result)
check(result, expected)

# Factorize some integers

result1 = factorize(2016)
expected1 = [2, 2, 2, 2, 2, 3, 3, 7]
print("Prime factorization of 2016:\t\t", result1)
check(result1, expected1)

result2 = factorize(2017)
expected2 = [2017]
print("Prime factorization of 2017:\t\t", result2)
check(result2, expected2)

result3 = factorize(999999999990)
expected3 = [2, 3, 3, 5, 21649, 513239]
print("Prime factorization of 999999999990:\t", result3)
check(result3, expected3)

result4 = factorize(999999999989)
expected4 = [999999999989]
print("Prime factorization of 999999999989:\t", result4)
check(result4, expected4)

print("Overall factorize functionality")
check([result1, result2, result3, result4], [expected1, expected2, expected3, expected4])