# -*- coding: utf-8 -*-
"""
Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer 
and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.
"""

class Node:

   def __init__(self, value):
      self.left = None
      self.right = None
      self.value = value
      
   def GetValue(self):
      if self.value.isnumeric():
          return self.value    
      else:
          return str(eval(self.left.GetValue()+self.value+self.right.GetValue()))   
    
 
def EvaluateTree(root):
    return float(root.GetValue())


root = Node("*")
root.left = Node("+")
root.right = Node("+")
root.left.left = Node('3')
root.left.right = Node('2')
root.right.left = Node('4')
root.right.right = Node('5')


print(EvaluateTree(root))

