"""
This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should
"""

def find_minimum_rooms(data):
    starts = [el[0] for el in data]
    ends =   [el[1] for el in data]
    s_idx = e_idx = max_overload = current_overload = 0
    while s_idx < len(data):
        if starts[s_idx] <= ends [e_idx]:
            current_overload+=1
            max_overload = max(max_overload,current_overload)
            s_idx+=1
        else:
            e_idx+=1
            
    return max_overload


data = [(30, 75), (0, 50), (60, 150)]
print(find_minimum_rooms(data))
