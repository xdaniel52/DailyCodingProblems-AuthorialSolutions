"""
Compute the running median of a sequence of numbers. That is, given a stream of numbers, 
print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2
"""

from  statistics import median


def running_median_easiest(stream):
    for i in range(len(stream)):
        print(median(stream[:i+1]))

def running_median(stream):
    l = stream.copy()
    for i in range(len(stream)):
        for j in range(i):
            if l[j] > l[i]:
                l.insert(j, l.pop(i))
                break
        if i%2 ==0:
            print(l[i//2])           
        else:
            print((l[i//2]+l[i-i//2])/2)


a = [2, 1, 5, 7, 2, 0, 5]
running_median(a)
