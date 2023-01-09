"""
This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, 
and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.                    |
"""

def find_last_prisoner_idx(N,k):
    tab = [i for i in range(1,N+1)]
    idx = k-1
    tab_len = N
    while tab_len > 1:
        poped = 0
        while idx < tab_len:  
            tab.pop(idx-poped) 
            poped+=1     
            idx+=k

        idx=idx%tab_len
        tab_len= len(tab)
    return tab[0]


print(find_last_prisoner_idx(5,2))
