"""
This problem was asked by Uber.

Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.

For example, given k = 18 and the following binary tree:

    8
   / \
  4   13
 / \   \
2   6   19
Return True since the path 8 -> 4 -> 6 sums to 18.
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
    def find_sum_path(self, sum_val):
        reduced_sum = sum_val - self.val
        
        if self.left == None and self.right == None:
            if reduced_sum  == 0:
                return True
            else:
                return False
        
        first = False if self.left == None else self.left.find_sum_path(reduced_sum)
        second = False if self.right == None else self.right.find_sum_path(reduced_sum)

        return first or second



root = Node(8)
root.left = Node(4)
root.right = Node(13)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.right = Node(19)

print(root.find_sum_path(18))





