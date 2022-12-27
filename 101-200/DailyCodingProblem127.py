"""
This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the number. 
The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class NumberAsLinkedList:
    def __init__(self, number):
        self.first = Node(number%10)
        current_node = self.first
        number = number // 10
        while number > 0:
            current_node.next = Node(number%10)
            current_node = current_node.next
            number = number // 10

    def __str__(self):
        result = str(self.first.value)
        current_node = self.first.next
        while current_node != None:
            result += " -> "+str(current_node.value)
            current_node = current_node.next          
        return result
    
    
def sum_numbers(num1 :Node,num2 :Node):
    result = NumberAsLinkedList(0)
    current_node = result.first
    current_node1 = num1.first
    current_node2 = num2.first
    while not (current_node1 == None and current_node2 == None):
        current_node.next = Node(0)
        if current_node1 != None:
           current_node.value += current_node1.value
           current_node1 = current_node1.next
           
        if current_node2 != None:
           current_node.value += current_node2.value
           current_node2 = current_node2.next
           
        if current_node.value > 9:
           current_node.value = current_node.value%10
           current_node.next.value = 1
           
        if current_node1 == None and current_node2 == None and current_node.next.value == 0:           
           current_node.next = None 
        else:
           current_node = current_node.next
        
    return result
    
number = NumberAsLinkedList(54321)
print(number)
print()

number1 = NumberAsLinkedList(99)
number2 = NumberAsLinkedList(25)
print(sum_numbers(number1,number2))
