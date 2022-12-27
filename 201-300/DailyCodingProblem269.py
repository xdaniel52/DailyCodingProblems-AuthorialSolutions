"""
This problem was asked by Microsoft.

You are given an string representing the initial conditions of some dominoes. 
Each element can take one of three values:

L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling. Note that 
if a domino receives a force from the left and right side simultaneously, it will remain upright.

For example, given the string .L.R....L, you should return LL.RRRLLL.

Given the string ..R...L.L, you should return ..RR.LLLL.
"""

def Find_Domino_Orientation(s):
    init = list(s)
    result = init.copy()
    r_idx = None
    for i in range(len(init)):
        if init[i] == 'L':
            if r_idx is not None:
                k=r_idx+(i-r_idx)//2
                if k%2==0:
                    result[k] = '.'
                for j in range(k+1,i):
                    result[j]= 'L'         
            else:
                j=i
                while result[j-1] =='.':
                    result[j-1]= 'L'
                    j-=1
                          
            r_idx = None
        elif init[i] == 'R':
            r_idx = i
            j=i
            while result[j+1] =='.':
                result[j+1]= 'R'
                j+=1
    
    return "".join(result)


print(Find_Domino_Orientation(".L.R....L"))

print(Find_Domino_Orientation("..R...L.L"))
