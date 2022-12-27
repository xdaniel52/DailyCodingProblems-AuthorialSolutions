"""
This problem was asked by Google.

UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. 
The rules for mapping characters are as follows:

For a single-byte character, the first bit must be zero.
For an n-byte character, the first byte starts with n ones and a zero. 
The other n - 1 bytes all start with 10.
Visually, this can be represented as follows.

 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Write a program that takes in an array of integers representing byte values, 
 returns whether it is a valid UTF-8 encoding.
"""
import numpy as np

def Check_UTF8_Encoding(arr):
    if len(arr) % 8 != 0:
        return False
    bytes_arr = list(np.reshape(arr, (len(arr)//8,8)))
    idx = 0
    while idx < len(bytes_arr):
        o_idx = np.where(bytes_arr[idx]==0)[0]
        if len(o_idx)==0:
            return False
        o_idx = o_idx[0]
        if o_idx < 5:
            for i in range(o_idx-1):
                idx+=1
                if not (bytes_arr[idx][0]==1 and bytes_arr[idx][1]==0):
                      return False
        else:
            return False
    
        idx+=1
    return True


print(Check_UTF8_Encoding([1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0]))

print(Check_UTF8_Encoding([1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,0,1,0,1,0,1,1,0,0]))

print(Check_UTF8_Encoding([1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,1,1,0,1,1,0,0]))

print(Check_UTF8_Encoding([1,1,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1,0,0]))

print(Check_UTF8_Encoding([0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,0]))















