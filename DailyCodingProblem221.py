"""
This problem was asked by Zillow.

Let's define a "sevenish" number to be one which is either a power of 7, 
or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. 
Create an algorithm to find the nth sevenish number.
"""

def Sevenish(n):
    arr=[1]
    power_num = 1
    while len(arr) < n:
        next_pow = pow(7,power_num)
        arr.append(next_pow)
        power_num+=1
        for el in arr[:-1]:
             arr.append(el + next_pow)

    return arr[n-1]

for i in range(1,100):
    print(Sevenish(i))









 
