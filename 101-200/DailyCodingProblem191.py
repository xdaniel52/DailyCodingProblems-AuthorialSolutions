"""
This problem was asked by Stripe.

Given a collection of intervals, find the minimum number of intervals you need 
to remove to make the rest of the intervals non-overlapping.

Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.

For example, given the intervals (7, 9), (2, 4), (5, 8), 
return 1 as the last interval can be removed and the first two won't overlap.

The intervals are not necessarily sorted in any order.
"""


def number_of_overlapping(array :list):
    counter = 0
    while True:
        overlappings = [1 for _ in range(len(array))]
        max_idx = 1
        for i in range(len(array)):
            for j in range(len(array)):
                if i!=j:
                    if (array[i][0] >= array[j][0] and array[i][0] <= array[j][1])\
                        or (array[i][1] > array[j][0] and array[i][1] < array[j][1]):
                        overlappings[i]+=1
            if overlappings[i] > overlappings[max_idx]:
                max_idx = i
                         
        if overlappings[max_idx] == 1:
            break               
        
        array.pop(max_idx) 
        counter+=1                 

    return counter              
                    

intervals = [(7, 9), (2, 4), (5, 8)]

print(number_of_overlapping(intervals))
