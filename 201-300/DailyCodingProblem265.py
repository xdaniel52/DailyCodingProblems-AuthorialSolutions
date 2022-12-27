"""
This problem was asked by Atlassian.

MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. 
They would like to give the smallest positive amount to each worker consistent with the constraint 
that if a developer has written more lines of code than their neighbor, they should receive more money.

Given an array representing a line of seats of employees at MegaCorp, determine how much each one 
should get paid.

For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1]. 
"""

def calc_bonuses(arr):
    bonuses = [1 for _ in range(len(arr))]
    idx = 0
    for i in range(1, len(arr)):
        print( bonuses)
        if arr[i] > arr[i-1]: 
           bonuses[i] = bonuses[i-1] +1
           idx = i
        elif  arr[i] < arr[i-1]:
           bonuses[idx+1:i] = [b+1 for b in bonuses[idx+1:i]]  
        
    return bonuses
    
print(calc_bonuses([10, 40, 200, 1000, 60, 30]))