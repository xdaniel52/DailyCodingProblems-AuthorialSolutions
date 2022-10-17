"""
This problem was asked by Google.

Given an array of elements, return the length of the longest subarray where
 all its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as 
the longest subarray of distinct elements is [5, 2, 3, 4, 1].
"""


def FindLengthSubArray(array):
    sub =[]
    max_len = 0
    for e in array:
        while e in sub:
            sub.pop(0)    
        sub.append(e)
        max_len = max(max_len,len(sub))
    return max_len


test_array =  [5, 1, 3, 5, 2, 3, 4, 1]
print(FindLengthSubArray(test_array))


test_array =  [1,2,3,4,3,1,2,4,5,6,3,6]
print(FindLengthSubArray(test_array))
