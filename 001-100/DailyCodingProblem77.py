"""
This problem was asked by Snapchat.

Given a list of possibly overlapping intervals, return a new list of intervals where 
all overlapping intervals have been merged.

The input list is not necessarily ordered in any way.

For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].
"""

def mearge(interval1,interval2):
    return (min(interval1[0],interval2[0]),max(interval1[1],interval2[1]))

def mearge_intervals(intervals):
    i=0
    while i < len(intervals)-1:
        j = i+1
        while j < len(intervals):
            if intervals[i][0] >= intervals[j][0] and intervals[i][0] <= intervals[j][1] or \
               intervals[i][1] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                      intervals[j] = mearge(intervals[i],intervals[j])
                      intervals.pop(i)
                      i-=1
                      break
            j+=1
        i+=1
    return intervals     


print(mearge_intervals([(1, 3), (5, 8), (4, 10), (20, 25)]))

print(mearge_intervals([(1, 4), (5, 8), (4, 10), (20, 25),(24,28),(28,30)]))
