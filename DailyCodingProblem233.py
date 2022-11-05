"""
This problem was asked by Apple.

Implement the function fib(n), which returns the nth number in the Fibonacci sequence, 
using only O(1) space.
"""

def nth_fib(n):
    a=b=1
    for i in range(2,n):
        a,b = b,a+b          
    return b


for i in range(1,10):
    print(nth_fib(i))