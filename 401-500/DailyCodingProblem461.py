"""
This problem was asked by Facebook.

On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. 
One power of the Qux is that if two of them are standing next to each other, they can transform 
into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible 
sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
"""

def transform_quxes(q1,q2):
    if q1 != 'R' and q2 != 'R':
        return 'R'
    elif q1 != 'G' and q2 != 'G':
        return 'G'
    else:
        return 'B'

def find_remaining_quxes(qux_line: list):
    min_group = qux_line.copy()
    for i in range(len(qux_line)-1):

        if len(min_group) == 1:
            break

        if qux_line[i] != qux_line[i+1]:
            tmp_qux_line = qux_line.copy()
            tmp_qux_line[i:i+2] =  transform_quxes(qux_line[i] ,qux_line[i+1] ) 
            min_line = find_remaining_quxes(tmp_qux_line)
            if len(min_line) < len(min_group):
                min_group = min_line
    
    return min_group

def find_min_remaining_quxes(qux_line: list):
    return len(find_remaining_quxes(qux_line))


line = ['R', 'G', 'B', 'G', 'B']
print(find_min_remaining_quxes(line))

line = ['R', 'G', 'B', 'B', 'B','B']
print(find_min_remaining_quxes(line))
