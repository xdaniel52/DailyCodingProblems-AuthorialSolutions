"""
This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""

def dict_flatten(dictionary, prefix=""):
    result = {}
    for key in dictionary.keys():
        if type(dictionary[key]) is dict:
            result.update(dict_flatten(dictionary[key],prefix+key+'.'))
        else:
            result[prefix+key] = dictionary[key]
            
    return result

test_dict = \
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}

print(dict_flatten(test_dict))