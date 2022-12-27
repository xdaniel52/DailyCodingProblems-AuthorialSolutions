"""
This problem was asked by Stripe.

Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.

For example, given 156, you should return 3.
"""

def len_longest_seq_of_ones(n):
    n_str = format(156,"b")
    max_len = 0
    counter = 0
    for num in n_str:
        if num == "1":
            counter+=1
        else:
            if counter > max_len:
                max_len = counter
                counter = 0
                
    if counter > max_len:
        max_len = counter
        counter = 0
        
    return max_len
    
print(len_longest_seq_of_ones(156))
