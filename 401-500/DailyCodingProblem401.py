"""
This problem was asked by Twitter.

A permutation can be specified by an array P, where P[i] represents the location 
of the element at i in the permutation. For example, [2, 1, 0] represents 
the permutation where elements at the index 0 and 2 are swapped.

Given an array and a permutation, apply the permutation to the array. For example,
 given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].
"""

def apply_permutation(arr,perm):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr[perm[i]])
        
    return new_arr

array = ["a", "b", "c"]
permutation = [2, 1, 0]
print(apply_permutation(array,permutation))
