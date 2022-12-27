"""
This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, 
as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
"""


def check_integer_palindrome(value):
    arr=[]
    while value > 0:
        arr.append(value%10)
        value=value//10    
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:       
            return False
        
    return True


print(check_integer_palindrome(121))

print(check_integer_palindrome(888))

print(check_integer_palindrome(678))