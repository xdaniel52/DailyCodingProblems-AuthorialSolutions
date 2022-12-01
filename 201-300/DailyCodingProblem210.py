"""
This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?
"""


def Test(number):
    longest_seq_for = 0
    longest_seq_length = 0
    for i in range(1,number):
        seq = Collatz_seq(i)
        if len(seq) > longest_seq_length:
            longest_seq_length = len(seq)
            longest_seq_for = seq
            
    return longest_seq_length

def Collatz_seq(n):
    result = [n]
    while n != 1:
        if n%2 == 0:
            n=n//2
        else:
            n=3*n+1
        result.append(n)
             
        
    return result


print(Test(1000000))








