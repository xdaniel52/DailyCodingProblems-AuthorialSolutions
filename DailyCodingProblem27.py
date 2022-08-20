"""
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false
"""

def bracketsCheck(given_string : str) -> bool:
    if given_string == "":
        return True 
    
    if given_string[0] == '(':
        searchCharacter = ')'
    elif given_string[0] == '[':
        searchCharacter = ']'
    elif given_string[0] == '{':
        searchCharacter = '}'
    else:
        return False
    
    try:
        close_id = given_string.index(searchCharacter)
        counter = given_string[1:close_id].count(given_string[0])
        if counter > 0:
            for i in range(counter):
                close_id = given_string[close_id+1:].index(searchCharacter)
                 
        if close_id == len(given_string)-1:
            return bracketsCheck(given_string[1:close_id])
        else:
            return bracketsCheck(given_string[1:close_id]) and bracketsCheck(given_string[close_id+1:])

    except Exception:
        return False
    

print(bracketsCheck('([])[]({})'))

print(bracketsCheck('([)]'))

print(bracketsCheck('((()'))
