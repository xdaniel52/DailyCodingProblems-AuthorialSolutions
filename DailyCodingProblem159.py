"""
This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""

def First_Recurring_Character(string):
    characters = []
    for l in string:
        if l in characters:
            return l
        else:
            characters.append(l)
            
    return None


string1 = 'acbbac'
print(First_Recurring_Character(string1))

string2 = 'abcdef'
print(First_Recurring_Character(string2))