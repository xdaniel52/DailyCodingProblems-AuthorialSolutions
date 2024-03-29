"""
This problem was asked by Google.

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
"""

class Node:

   def __init__(self, value):
      self.left = None
      self.right = None
      self.value = value
       
      
def find_deepest_node_in_tree(root :Node):
    deepest, _ = find_helper(root)
    return deepest

def find_helper(node :Node):
    if node.left == None and node.right == None:
        deepest = node 
        depth = 1
    else:
        depth = None
        if node.left != None:
            deepest, depth = find_helper(node.left)
        if node.right != None:
            deepest_right, depth_right = find_helper(node.right)
        
            if depth == None or depth < depth_right:
                deepest = deepest_right
                depth = depth_right   
    return (deepest,depth+1)
    

root = Node("a")
root.left = Node("b")
root.right = Node("c")
root.left.left = Node('d')
print(find_deepest_node_in_tree(root).value)


root = Node("a")
root.left = Node("b")
root.right = Node("c")
root.left.left = Node('d')
root.right.right = Node('e')
root.right.left = Node('f')
root.right.right.right = Node('g')
print(find_deepest_node_in_tree(root).value)

