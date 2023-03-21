"""
This problem was asked by Google.

You are given an M by N matrix consisting of booleans that represents a board. 
Each True boolean represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps 
required to reach the end coordinate from the start. If there is no possible path, then return null. 
You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board
"""

#from functools import functools_iru_cache

#$@functools_iru_cache() 
def find_path(matrix, start, end):

    if start[-1] == end:
       return 0
    if matrix[start[-1][0]][start[-1][1]] == True:
        return None
    if start[-1] in start[:-1]:
        return None
      
    shortest = None
    horizontal_diff = end[1]  - start[-1][1]
    vertical_diff = end[0] - start[-1][0]  
    order = [3,1,4,2]
    if(horizontal_diff > 0):
        order[0] = 4
        order[2] = 3
    if(vertical_diff > 0):
        order[1] = 2
        order[3] = 1
    
    for o in order:
        new_path = None
        if o == 1 and start[-1][0] != 0: #1 up
            new_path = start.copy()
            new_path.append((start[-1][0]-1,start[-1][1]))         
                        
        if o == 2 and start[-1][0] != len(matrix)-1: #2 down
            new_path = start.copy()
            new_path.append((start[-1][0]+1,start[-1][1]))
            
        if o == 3 and start[-1][1] != 0:
            new_path = start.copy() #3 left 
            new_path.append((start[-1][0],start[-1][1]-1))

        if o == 4 and start[-1][1] != len(matrix[0])-1: # 4 right
            new_path = start.copy()
            new_path.append((start[-1][0],start[-1][1]+1))
         
        if new_path is not None:
            path_len = find_path(matrix, new_path, end)
            if path_len is not None:                
                if shortest is None or path_len < shortest:
                    shortest = path_len       
            if shortest is not None and order.index(o) == 1:
                return shortest + 1
                
    if shortest is None:
        return shortest
    else:
        return shortest+1


mat = [[False,False,False,False],
       [True,True,False,True],
       [False,False,False,False],
       [False,False,False,False],]

mat2 = [[False,False,False,False],
       [True,True,False,True],
       [False,False,False,False],
       [False,True,True,True],
       [False,False,False,False],
       [True,True,True,False],
       [False,False,False,False],]

start_point = [(6,0)]
end_point = (0,0)

print(find_path(mat2, start_point, end_point))