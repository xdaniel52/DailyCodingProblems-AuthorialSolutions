"""
This problem was asked by Amazon.

A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node. 
The following tree is an example:

        4
      / | \
    3   5   3
  /           \
9              9
Given a k-ary tree, determine whether it is symmetric.
"""

class Node:
    def __init__(self, value, k):  
        self.value = value
        self.children = [None for i in range(k)]
    def Add(self, idx, node):
        self.children[idx] = node

def Check_Symmetricity(root, k):
    tree = root
    for i in range(k // 2):
        Tree_Reverse(tree.children[-i-1],k)
        if not Nodes_Comparer(tree.children[i],tree.children[-i-1],k):
            return False
        
    return True
    
        
    
def Tree_Reverse(root, k):
    if root is None:
        return
    else:
        for i in range(k // 2):
            root.children[i], root.children[-i-1] = root.children[-i-1], root.children[i]
            Tree_Reverse(root.children[i],k)
            Tree_Reverse(root.children[-i-1],k)

def Nodes_Comparer(n1, n2, k):
    if n1 is None and n2 is None:
        return True
    elif (n1 is None and n2 is not None) \
      or (n1 is not None and n2 is None) \
      or n1.value != n2.value:
        return False  
    else:
        for i in range(k):
            if not Nodes_Comparer(n1.children[i],n2.children[i],k):
                return False
    return True
            
            
            
root = Node(4,3)
root.Add(0, Node(3,3))          
root.Add(1, Node(5,3)) 
root.Add(2, Node(3,3)) 
root.children[0].Add(0, Node(9,3)) 
root.children[2].Add(2, Node(9,3)) 
print(Check_Symmetricity(root,3))    
  

root = Node(4,2)
root.Add(0, Node(5,2))           
root.Add(1, Node(5,2)) 
root.children[0].Add(0, Node(6,2)) 
root.children[1].Add(1, Node(6,2)) 
print(Check_Symmetricity(root,2))           
      
      
root = Node(4,2)
root.Add(0, Node(5,2))           
root.Add(1, Node(5,2)) 
root.children[0].Add(0, Node(6,2)) 
root.children[1].Add(1, Node(5,2))   
print(Check_Symmetricity(root,2)) 