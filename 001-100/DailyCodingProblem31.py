"""
The edit distance between two strings refers to the minimum number of character insertions, 
deletions, and substitutions required to change one string to the other. For example, 
the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, 
substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

def edit_dictance(s1,s2):
    s1_len = len(s1)
    s2_len = len(s2)
    if s1_len == s2_len:
        return helpper(s1, s2)
    elif s1_len < s2_len:
        min_counter = s2_len
        for i in range(s2_len-s1_len+1):
            count = helpper(s1, s2[i:i+s1_len])
            if count < min_counter:
                min_counter = count
        
        return min_counter + (s2_len-s1_len)
    else:
        return edit_dictance(s2,s1)
        
def helpper(s1,s2):
    counter = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            counter+=1
    return counter


print(edit_dictance("kitten","sitting"))
print(edit_dictance("sitting","kitten"))
print(edit_dictance("123","4567123"))