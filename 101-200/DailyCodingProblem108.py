"""
This problem was asked by Google.

Given two strings A and B, return whether or not A can be shifted some number of times to get B.

For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.
"""

def check_shiftable(A,B):
    for _ in range(len(A)):
        if A==B:
            return True      
        A = A[-1]+A[:-1]
        
    return False
 
A = "abcde"
B = "cdeab"
print(check_shiftable(A,B))

A = "abc"
B = "acb"
print(check_shiftable(A,B))