"""
This problem was asked by Oracle.

Given a binary search tree, find the floor and ceiling of a given integer. 
The floor is the highest element in the tree less than or equal to an integer, 
while the ceiling is the lowest element in the tree greater than or equal to an integer.

If either value does not exist, return None.
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def Find_floor_and_ceiling_in_tree(tree, number):
     local_floor = tree.val if tree.val>=number else None
     local_ceiling = tree.val if tree.val<=number else None
     if tree.left is not None:
         left_floor,left_ceiling = Find_floor_and_ceiling_in_tree(tree.left,number)
         if local_floor is None or (left_floor is not None and left_floor>=number and left_floor<local_floor):
             local_floor = left_floor 
         if local_ceiling is None or (left_ceiling is not None and left_ceiling<=number and left_ceiling>local_ceiling):
             local_ceiling = left_ceiling 
     if tree.right is not None:
         right_floor,right_ceiling = Find_floor_and_ceiling_in_tree(tree.right,number) 
         if local_floor is None or (right_floor is not None and right_floor>=number and right_floor<local_floor):
             local_floor = right_floor 
         if local_ceiling is None or (right_ceiling is not None and right_ceiling<=number and right_ceiling>local_ceiling):
             local_ceiling = right_ceiling 
     return [local_floor,local_ceiling]
    

root = Node(8) 
root.left = Node(4)
root.right = Node(13)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.right = Node(19)


print(Find_floor_and_ceiling_in_tree(root,5))

print(Find_floor_and_ceiling_in_tree(root,20))

print(Find_floor_and_ceiling_in_tree(root,8))





