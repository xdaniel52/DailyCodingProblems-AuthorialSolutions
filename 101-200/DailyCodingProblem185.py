
"""
This problem was asked by Google.

Given two rectangles on a 2D graph, return the area of their intersection. 
If the rectangles don't intersect, return 0.

For example, given the following rectangles:

{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
}
and

{
    "top_left": (0, 5),
    "dimensions": (4, 3) # width, height
}
return 6.
"""

def Calculate_Intersection(rec1,rec2):
    
    rec1left = rec1["top_left"][0]
    rec1rigth = rec1["top_left"][0] + rec1["dimensions"][0]
    rec2left = rec2["top_left"][0]
    rec2rigth = rec2["top_left"][0] + rec2["dimensions"][0]

    width = min(rec1rigth,rec2rigth) - max(rec1left,rec2left)
    
    if width<=0:
        return 0
    
    rec1top = rec1["top_left"][1]
    rec1bot = rec1["top_left"][1] - rec1["dimensions"][1]
    rec2top = rec2["top_left"][1]
    rec2bot = rec2["top_left"][1] - rec2["dimensions"][1]   
    
    height = min(rec1top,rec2top) - max(rec1bot,rec2bot)
    
    if height<=0:
        return 0

    return width*height



rectangle1={
    "top_left": (1, 4),
    "dimensions": (3, 3) 
}

rectangle2={
    "top_left": (0, 5),
    "dimensions": (4, 3) 
}  
    
print(Calculate_Intersection(rectangle1,rectangle2))


