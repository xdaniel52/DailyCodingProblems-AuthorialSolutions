"""
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""

import itertools

def Find_nth_perfect_number(n):
    ith_perfect = 0
    
    for i in itertools.count():
        ith_sum = 0
        tmp_i = i
        while(tmp_i):
            ith_sum+=tmp_i%10
            tmp_i=tmp_i//10
            
        if ith_sum == 10:
            ith_perfect +=1
            if ith_perfect == n:
                return i
            

print(Find_nth_perfect_number(1))
print(Find_nth_perfect_number(2))

