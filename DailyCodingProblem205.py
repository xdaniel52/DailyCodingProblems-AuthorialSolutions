"""
This problem was asked by IBM.

Given an integer, find the next permutation of it in absolute order. For example, given 48975, 
the next permutation would be 49578.
"""

def FindNextAbsolutePermutation(number):
    tmp_number = number
    arr=[]
    while tmp_number > 0:
        arr.insert(0,tmp_number%10)
        tmp_number=tmp_number//10  

    for i in range(len(arr)-2,-1,-1):
        if arr[i] < arr[i+1]:
            arr[i+2:] = sorted(arr[i+2:])
            arr.append(arr.pop(i))
            break
            
    result = arr[0]
    for i in range(1,len(arr)):
        result*=10
        result+=arr[i]
    
    return result
    
print(FindNextAbsolutePermutation(48975))
    
    

