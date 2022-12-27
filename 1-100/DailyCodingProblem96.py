"""
This problem was asked by Microsoft.

Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].
"""

def find_permutations(given_list):
    list_len = len(given_list)
    if list_len == 1:
        return [given_list]
    elif list_len == 2:
        return [given_list,[given_list[1],given_list[0]]]
    else:
        result = []
        for i in range(list_len):
            tmp_list = find_permutations(given_list[:i]+given_list[i+1:])
            result+= [ [given_list[i]] + j for j in tmp_list]
        return result

print(find_permutations([1,2,3]))
