"""
This problem was asked by Facebook.

Given a list of integers, return the largest product that can be made by multiplying any three integers.

For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.

You can assume the list has at least three integers.
"""

def find_largest_product_ln_list(given_list):
    max1,max2,max3 = tuple(sorted(given_list[:3],reverse = True))
    min1 = max3
    min2 = max2
    for e in given_list[3:]:
        if e > max3:
            if e > max2:
                if e > max1:
                    max3=max2
                    max2=max1
                    max1 = e
                else:
                    max3=max2
                    max2 = e
            else:
                max3 = e
        elif e < min2:
            if e < min1:
                min2 = min1
                min1 = e
            else:
                min2 = e
            
    return max(max1*max2*max3,max1*min1*min2)
    

list_of_integers = [-10, -10, 5, 2]

print(find_largest_product_ln_list(list_of_integers))
