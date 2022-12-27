
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

def calculate_intersection(rec1,rec2):
    
    rec1_left = rec1["top_left"][0]
    rec1_rigth = rec1["top_left"][0] + rec1["dimensions"][0]
    rec2_left = rec2["top_left"][0]
    rec2_rigth = rec2["top_left"][0] + rec2["dimensions"][0]

    width = min(rec1_rigth,rec2_rigth) - max(rec1_left,rec2_left)
    
    if width<=0:
        return 0
    
    rec1_top = rec1["top_left"][1]
    rec1_bot = rec1["top_left"][1] - rec1["dimensions"][1]
    rec2_top = rec2["top_left"][1]
    rec2_bot = rec2["top_left"][1] - rec2["dimensions"][1]   
    
    height = min(rec1_top,rec2_top) - max(rec1_bot,rec2_bot)
    
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
    
print(calculate_intersection(rectangle1,rectangle2))


