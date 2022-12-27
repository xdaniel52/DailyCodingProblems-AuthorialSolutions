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
    def __init__(self, value, children_num):  
        self.value = value
        self.children = [None for _ in range(children_num)]
    def add(self, idx, node):
        self.children[idx] = node

def check_symmetricity(root :Node, children_num):
    tree = root
    for i in range(children_num // 2):
        tree_reverse(tree.children[-i-1], children_num)
        if not nodes_comparer(tree.children[i], tree.children[-i-1], children_num):
            return False
        
    return True
    
def tree_reverse(root :Node, children_num):
    if root is None:
        return
    else:
        for i in range(children_num // 2):
            root.children[i], root.children[-i-1] = root.children[-i-1], root.children[i]
            tree_reverse(root.children[i], children_num)
            tree_reverse(root.children[-i-1], children_num)

def nodes_comparer(node1 :Node, node2 :Node, children_num):
    if node1 is None and node2 is None:
        return True
    elif (node1 is None and node2 is not None) \
      or (node1 is not None and node2 is None) \
      or node1.value != node2.value:
        return False  
    else:
        for i in range(children_num):
            if not nodes_comparer(node1.children[i], node2.children[i], children_num):
                return False
    return True
            
                     
root = Node(4,3)
root.add(0, Node(3,3))          
root.add(1, Node(5,3)) 
root.add(2, Node(3,3)) 
root.children[0].add(0, Node(9,3)) 
root.children[2].add(2, Node(9,3)) 
print(check_symmetricity(root,3))    
  

root = Node(4,2)
root.add(0, Node(5,2))           
root.add(1, Node(5,2)) 
root.children[0].add(0, Node(6,2)) 
root.children[1].add(1, Node(6,2)) 
print(check_symmetricity(root,2))           
      
      
root = Node(4,2)
root.add(0, Node(5,2))           
root.add(1, Node(5,2)) 
root.children[0].add(0, Node(6,2)) 
root.children[1].add(1, Node(5,2))   
print(check_symmetricity(root,2)) 
