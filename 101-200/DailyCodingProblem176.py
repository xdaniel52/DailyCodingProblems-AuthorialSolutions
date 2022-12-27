"""
This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""

def check_mapping(s1,s2):
    
    if len(s1) != len(s2):
        return False
    
    mapping = {}
    for l1,l2 in zip(s1,s2):
        if l1 in mapping.keys():
            if mapping[l1] != l2:
                return False
        else:
            mapping[l1] = l2
                
    return True

s1 = "abc" 
s2 = "bcd"
print(check_mapping(s1,s2))

s1 = "foo" 
s2 = "bar"
print(check_mapping(s1,s2))

