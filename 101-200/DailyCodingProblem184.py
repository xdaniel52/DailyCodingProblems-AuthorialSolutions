"""
This problem was asked by Amazon.

Given n numbers, find the greatest common denominator between them.

For example, given the numbers [42, 56, 14], return 14
"""


def gcd(arr):
    denominators = []
    for i in range(1,arr[0]//2):
        if arr[0]%i==0:
            denominators.append(i)
            
    for num in arr[1:]:
        i = 0
        while i != len(denominators):
            if num%denominators[i] != 0:
                denominators.pop(i)
            else:
                i+=1
                     
    return denominators[-1]

print(gcd([42, 56, 14]))
                