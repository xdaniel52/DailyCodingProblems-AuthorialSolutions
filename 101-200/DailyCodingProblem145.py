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
   
    def Add(self, value):
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next 
        currentNode.next = Node(value)     
        
    def __str__(self):
        result = str(self.head.value)
        currentNode = self.head.next
        while currentNode != None:
            result += " -> "+str(currentNode.value)
            currentNode = currentNode.next          
        return result
  
        
def SwapEveryTwoNodes(head):
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
linked_list.Add(2)
linked_list.Add(3)
linked_list.Add(4)
print(linked_list)

SwapEveryTwoNodes(linked_list.head)

print(linked_list)

#test2
linked_list = SingleLinkedList(1)
linked_list.Add(2)
linked_list.Add(3)
linked_list.Add(4)
linked_list.Add(5)
linked_list.Add(6)
linked_list.Add(7)
print(linked_list)

SwapEveryTwoNodes(linked_list.head)

print(linked_list)


