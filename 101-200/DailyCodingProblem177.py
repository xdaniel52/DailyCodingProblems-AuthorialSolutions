"""
This problem was asked by Airbnb.

Given a linked list and a positive integer k, rotate the list to the right by k places.

For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.

Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2
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
    
    
def Rotate_List(list,k):
    node = list.head
    list_len = 1
    while node.next != None:
        list_len+=1
        node = node.next
    
    if k > list_len:
        k = k%list_len
    elif k == list_len:
        return 
    
    node.next = list.head
    
    node = list.head
    for i in range(list_len - k - 1):
        node = node.next
    
    list.head = node.next
    node.next = None
    
    
list = SingleLinkedList(7)
list.Add(7)
list.Add(3)   
list.Add(5)  
    
print(list)

Rotate_List(list,2)

print(list)
    
list = SingleLinkedList(1)
list.Add(2)
list.Add(3)   
list.Add(4)    
list.Add(5)
  
print(list)

Rotate_List(list,3)

print(list)