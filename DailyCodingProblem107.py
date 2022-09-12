"""
This problem was asked by Microsoft.

Print the nodes in a binary tree level-wise. 

For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5
"""

class Node:

   def __init__(self, value):
      self.left = None
      self.right = None
      self.value = value
       
      
def PrintTreeValues(root):
    level = 0
    elements = []
    while True:      
        if not PrintNodeLevel(root,level, elements):
            break
        level+=1
        
    result = ""
    for e in elements:
        result+=str(e)+", "
    
    print(result[:-2])     

def PrintNodeLevel(node,level,elements):
    if level == 0:
        elements.append(node.value)
        return True
    else:   
        level-=1
        if node.left != None:
            result1 = PrintNodeLevel(node.left,level,elements)
        else:
            result1 = False
        if node.right != None:
            result2 = PrintNodeLevel(node.right,level,elements)
        else:
            result2 = False   
        if result1 or result2:
            return True
        else:
            return False
    

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)
PrintTreeValues(root)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(8)
root.right.right.right.right = Node(9)
PrintTreeValues(root)
