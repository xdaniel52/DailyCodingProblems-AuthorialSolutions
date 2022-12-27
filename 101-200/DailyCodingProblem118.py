"""
This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
"""

def square_list(sorted_list):
    result_list = []
    add_idx = 0
    for e in sorted_list[:]:
        squared = e*e
        if e <= 0:
            result_list.insert(0, squared)
        else:         
            while True:
                if squared <= result_list[add_idx]:
                    result_list.insert(add_idx, squared)
                    break
                else:
                    add_idx+=1
                    if add_idx == len(result_list):
                        result_list.append(squared)                      
                        break            
    return result_list

sorted_list = [-9, -2, 0, 2, 3]
print(square_list(sorted_list))

sorted_list = [-100,-9,-5, -2, 0, 6, 8, 101]
print(square_list(sorted_list))
