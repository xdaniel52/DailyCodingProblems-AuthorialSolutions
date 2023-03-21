"""
This problem was asked by Google.

Given the head of a singly linked list, reverse it in-place.
"""

class Node:

   def __init__(self, value):
      self.next = None
      self.value = value


class SinglyLinkedList:

    def __init__(self, head: Node):
      self.head = head

    def AddValue(self, value):
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = Node(value)
        
    def Print_list(self):
        print("Values in list:")
        current_node = self.head
        while current_node.next != None:
            print(current_node.value)
            current_node = current_node.next
        print(current_node.value)
        
    def Reverse(self):
        if self.head.next == None:
            return
        elif self.head.next.next == None:
            self.head.next = self.head
            self.head = self.head.next      
            self.head.next = None
            return
            
        previous_node = self.head
        current_node = self.head.next
        next_node = self.head.next.next
        self.head.next = None
        while next_node != None:
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next
        current_node.next = previous_node
        self.head = current_node
        
        
linked_list = SinglyLinkedList(Node(1))      
linked_list.AddValue(2)
linked_list.AddValue(3)
linked_list.AddValue(4)

linked_list.Print_list()
linked_list.Reverse()
linked_list.Print_list()
        