"""
This problem was asked by Alibaba.

Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.

A solution will always exist. See Goldbach’s conjecture.

Example:

Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.

If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then

[a, b] < [c, d]
If a < c OR a==c AND b < d.
"""

def sieve_of_eratosthenes(n):
    result = []
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1

    for p in range(2, n+1):
        if primes[p]:
            result.append(p)
            
    return result
            
def find_two_primes(n):
    primes = sieve_of_eratosthenes(n)
    for prime in primes:
        if n-prime in primes:
            return [prime,n-prime]
        
    return None


for i in range(4,16,2):
    print(f"{i}: {find_two_primes(i)}")
