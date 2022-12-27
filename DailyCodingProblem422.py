"""
This problem was asked by Salesforce.

Write a program to merge two binary trees. Each node in the new tree should hold a value equal 
to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree 
should match that input node.
"""

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def MergeBinaryTrees(tree1 :Node,tree2:Node):
     result_tree = Node(tree1.val + tree2.val)
     
     if tree1.left is None and tree2.left is not None:
         result_tree.left = tree1.left
     elif tree1.left is not None and tree2.left is  None:
         result_tree.left = tree2.left
     elif tree1.left is not None and tree2.left is not None:
         result_tree.left = MergeBinaryTrees(tree1.left,tree2.left)
         
     if tree1.right is None and tree2.right is not None:
         result_tree.right = tree1.right
     elif tree1.right is not None and tree2.right is  None:
         result_tree.right = tree2.right
     elif tree1.right is not None and tree2.right is not None:
         result_tree.right = MergeBinaryTrees(tree1.right,tree2.right)
     
     return result_tree 
    

root1 = Node(8)
root1.left = Node(4)
root1.right = Node(13)
root1.left.left = Node(2)
root1.left.right = Node(6)
root1.right.right = Node(19)

root2 = Node(2)
root2.left = Node(1)
root2.right = Node(5)
root2.left.left = Node(10)

merged_tree = MergeBinaryTrees(root1,root2)



