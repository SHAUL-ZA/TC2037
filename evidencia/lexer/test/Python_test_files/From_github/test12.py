import math

# Function to calculate the Fibonacci sequence up to a given limit
def fibonacci_sequence(limit):
    sequence = [0, 1]
    while sequence[-1] < limit:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

# Function to calculate the nth prime number
def nth_prime_number(n):
    primes = [2]
    number = 3
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if number % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(number)
        number += 2
    return primes[-1]

# Function to calculate the sum of digits in a factorial number
def factorial_digit_sum(n):
    factorial = math.factorial(n)
    digit_sum = sum(int(digit) for digit in str(factorial))
    return digit_sum

# Function to calculate the nth term of the geometric series
def geometric_series_term(a, r, n):
    term = a * math.pow(r, n-1)
    return term

# Function to calculate the sum of an arithmetic series
def arithmetic_series_sum(a, d, n):
    last_term = a + (n - 1) * d
    series_sum = (n * (a + last_term)) / 2
    return series_sum

# Examples using the functions
fibonacci_limit = 100
fibonacci = fibonacci_sequence(fibonacci_limit)
print("Fibonacci sequence up to", fibonacci_limit, ":", fibonacci)

nth_prime = 10
nth_prime_number = nth_prime_number(nth_prime)
print("The", nth_prime, "prime number is:", nth_prime_number)

factorial_number = 5
factorial_sum = factorial_digit_sum(factorial_number)
print("Sum of digits in", factorial_number, "factorial:", factorial_sum)

a = 2
r = 3
n = 4
geometric_term = geometric_series_term(a, r, n)
print("The", n, "term of the geometric series is:", geometric_term)

a_arithmetic = 3
d_arithmetic = 2
n_arithmetic = 5
arithmetic_sum = arithmetic_series_sum(a_arithmetic, d_arithmetic, n_arithmetic)
print("Sum of the arithmetic series:", arithmetic_sum)
