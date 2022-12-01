"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false
"""

def Endoce(given_string : str) -> str:
    result = ""
    letter = given_string[0]
    counter = 1
    for i in range(1,len(given_string)):
        if given_string[i] == letter:
            counter += 1
        else:
            result+=str(counter)+letter
            letter = given_string[i]
            counter = 1

    result+=str(counter)+letter
    return result

def Decode(given_string : str) -> str:
    result = ""
    idx = 0
    for i in range(1,len(given_string)):
        if not given_string[i].isnumeric():
            result += given_string[i]*int(given_string[idx:i])
            idx = i+1

    return result

print(Endoce('AAAABBBCCDAA'))

print(Decode(Endoce('AAAABBBCCDAA')))
