"""
This problem was asked by Twitter.

A strobogrammatic number is a positive number that appears the same after being rotated 180 degrees. 
For example, 16891 is strobogrammatic.

Create a program that finds all strobogrammatic numbers with N digits.
"""

def FindStrobogrammaticNumbers(N):
    X = ['0','1','3','8','2','6','9','5']
    Y = ['0','1','3','8','5','9','6','2']
    
    number = ['0' for i in range(N)]
    for i in range((N+1)//2):
        for j in range(len(X)):
            



FindStrobogrammaticNumbers(3)
