"""
This problem was asked by Palantir.

The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. 
For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.

Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.
"""
import math


def Find_Egyption_Fraction(frac:tuple):
    result=[]
    n = frac[0]
    d = frac[1]
    while n > 0:
        new_denominator = math.ceil(d/n)
        result.append((1,new_denominator))
        n=n*new_denominator- d 
        d*=new_denominator
        
    return result
                      

print(Find_Egyption_Fraction((4,13)))