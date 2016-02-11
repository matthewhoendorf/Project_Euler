# The correct answer to Problem 3 is '6875'
print "\nThis program calculates the largest prime factor of a given number."
# User inputs number in which we'll calculate the prime factors
number = input("\nEnter a number: ")

# Store factors of a number in a list (excluding 1)
def factorsOf(n):
    factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            factors |= {i, div}
    return factors

# Boolean function that returns if a number is prime
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Filter the non-primes from a list of numbers
def primeFilter(factors):
    primeFactors = [factor for factor in factors if isPrime(factor) == True]
    return primeFactors

# Store the prime factors for the given number in a list
primeFactors = primeFilter(factorsOf(number))

# Output the prime factors
print "\nThe prime factors of %i are:" % number
print primeFilter(factorsOf(number))
# And finally, our solution
print "\nThe largest prime factor is:"
print max(primeFactors)
print ""
