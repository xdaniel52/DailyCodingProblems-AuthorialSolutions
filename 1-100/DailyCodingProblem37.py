"""
This problem was asked by Google.

The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
"""

def get_power_set(given_set : set):
    result = [set()]
    for el in given_set:
        for i in range(len(result)):
            tmp = result[i].copy()
            tmp.add(el)
            result.append(tmp)
    return result


print(get_power_set({1,2,3}))
