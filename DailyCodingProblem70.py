"""
This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.
"""

def Find_Nth_Perfect_Number(n):
    digits = [0,0,0,0,0,0,0,0,1,9]
    idx = 1
    while idx < n:
        digits[8]+=1
        if sum(digits[:9]) < 10 :
            digits[9] = 10 - sum(digits[:9])
        for i in range(8,0,-1):
                if digits[i] > 9:
                    digits[i-1] += 1
                    digits[i] = 0
                    
        while sum(digits) != 10:
            digits[8]+=1
            if sum(digits[:9]) < 10 :
                digits[9] = 10 - sum(digits[:9])
            for i in range(8,0,-1):
                if digits[i] > 9:
                    digits[i-1] += 1
                    digits[i] = 0
             
        idx+=1
    
    result = 0
    for i in range(10):
        result+=digits[9-i]*pow(10,i)
    return result
    

for i in range(1,100):
    print(Find_Nth_Perfect_Number(i))

