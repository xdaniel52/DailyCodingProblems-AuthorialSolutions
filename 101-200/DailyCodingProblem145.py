"""
This problem was asked by Google.

Given the head of a singly linked list, swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class SingleLinkedList:
    def __init__(self, value):
        self.head = Node(value)
   
    def add(self, value):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next 
        current_node.next = Node(value)     
        
    def __str__(self):
        result = str(self.head.value)
        current_node = self.head.next
        while current_node != None:
            result += " -> "+str(current_node.value)
            current_node = current_node.next          
        return result
  
        
def swap_every_two_nodes(head :Node):
    first_node = head
    second_node = first_node.next
    return_node = first_node
    first_node.value,second_node.value = second_node.value,first_node.value
    try:
        while True:
            first_node = second_node.next
            second_node = first_node.next
            first_node.value,second_node.value = second_node.value,first_node.value         
    except AttributeError:
        pass
    
    return return_node

#test1
linked_list = SingleLinkedList(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(4)
print(linked_list)

swap_every_two_nodes(linked_list.head)

print(linked_list)

#test2
linked_list = SingleLinkedList(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(4)
linked_list.add(5)
linked_list.add(6)
linked_list.add(7)
print(linked_list)

swap_every_two_nodes(linked_list.head)

print(linked_list)


