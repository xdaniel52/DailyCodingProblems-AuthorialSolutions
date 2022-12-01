"""
This problem was asked by Two Sigma.

Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, 
implement a function rand5() that returns an integer from 1 to 5 (inclusive).
"""

import random
def rand7():
    return random.randint(1, 7)

def rand5():
    matrix = [0,1,2,3,4,5,0,0]
    result = matrix[rand7()]
    while result == 0:
        result = matrix[rand7()]
    return result


print(rand5())
