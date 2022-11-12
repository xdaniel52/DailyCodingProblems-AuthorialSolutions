"""
This problem was asked by Square.

The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. 
The method is to take increasingly larger prime numbers, and mark their multiples as composite.

For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), 
then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, 
the unmarked numbers that remain will be prime.

Implement this algorithm.

Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).
"""

def Sieve_of_Eratosthenes(n):
    primes = []
    numbers=[True for i in range(0,n)]
    numbers[0] =  numbers[1] = False
    for i in range(0,n):
        if numbers[i]:
            for j in range(i*2,n,i):
                numbers[j] = False
            primes.append(i)

    return primes

print(Sieve_of_Eratosthenes(300))



import sys


def Bonus():
    primes = []
    multiples = []
    tab_len = 100
    numbers=[True for i in range(0,tab_len)]
    numbers[0] =  numbers[1] = False
    for i in range(2,sys.maxsize):
        if numbers[i%tab_len] == True:
            #for j in range(i*2,n,i):
            #    numbers[j] = False
            print(i)
            primes.append(i)
            multiples.append(2*i)
            
            while multiples[-1] < i// tab_len + tab_len:       
                if multiples[-1]%tab_len < 100:
                    numbers[multiples[-1]%tab_len] = False
                
                
                multiples[-1]+=primes[-1]
                    
            
        if i%tab_len == 0:
            numbers=[True for i in range(0,tab_len)]
            for p in range(len(primes)):
                while multiples[p] < i + tab_len:     
                    if multiples[p]%tab_len < 100:
                        numbers[multiples[p]%tab_len] = False
                        
                    multiples[p]+=primes[p]
                       

Bonus()

