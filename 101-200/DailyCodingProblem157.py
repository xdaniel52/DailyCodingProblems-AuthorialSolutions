"""
This problem was asked by Amazon.

Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, 
which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
"""

def determine_if_palindrome(string):
    letter_dict = {}
    for l in string:
        if l in letter_dict.keys():
            letter_dict[l]+=1
        else:
            letter_dict[l]=1

    odd_finded =True if len(string)%2 == 0 else False

    for val in letter_dict.values():
        if val%2 == 1:
            if odd_finded:
                return False
            else:
                odd_finded = True
    return True            


string1 = "carrace"
print(determine_if_palindrome(string1))

string2 = "daily"
print(determine_if_palindrome(string2))
