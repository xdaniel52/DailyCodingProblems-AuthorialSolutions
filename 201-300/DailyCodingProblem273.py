"""
This problem was asked by Apple.

A fixed point in an array is an element whose value is equal to its index. Given a sorted array 
of distinct elements, return a fixed point, if one exists. Otherwise, return False.

For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False
"""

def Find_Fixed_Point(arr):
    
    left_idx = 0
    right_idx = len(arr)-1
    while right_idx-left_idx>1:
        middle = (right_idx-left_idx)//2
        if arr[middle] == middle:
            return middle
        elif arr[middle] > middle:
            right_idx = middle-1
        else:
            left_idx = middle+1
            
    if arr[right_idx] ==right_idx:
        return right_idx
    elif arr[left_idx] ==left_idx:
        return left_idx
    else:
        return False

print(Find_Fixed_Point([-6, 0, 2, 40]))

print(Find_Fixed_Point([1, 5, 7, 8]))
