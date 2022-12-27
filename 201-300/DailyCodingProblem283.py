"""
This problem was asked by Google.

A regular number in mathematics is defined as one which evenly divides some power of 60. 
Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.

These numbers have had many applications, from helping ancient Babylonians keep 
time to tuning instruments according to the diatonic scale.

Given an integer N, write a program that returns, in order, the first N regular numbers.
"""

def find_regular_numbers(n):
    div=[2,3,5]
    result = {1}
    bound = 100
    while len(result) < 2*n:
        tmp = set()
        for res in result:
            for num in div:
                new_num = res*num
                while new_num < bound:
                    tmp.add(new_num)
                    new_num = new_num*num
        result=result.union(tmp)
        bound+=100
                         
    return sorted(list(result),key=lambda x: x)[:n]

print(find_regular_numbers(100))
    