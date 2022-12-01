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
        currentNode = self.first
        number=number // 10
        while number > 0:
            currentNode.next = Node(number%10)
            currentNode = currentNode.next
            number=number // 10

    def __str__(self):
        result = str(self.first.value)
        currentNode = self.first.next
        while currentNode != None:
            result += " -> "+str(currentNode.value)
            currentNode = currentNode.next          
        return result
    
    
def SumNumbers(num1,num2):
    result = NumberAsLinkedList(0)
    currentNode = result.first
    currentNode1 = num1.first
    currentNode2 = num2.first
    while not (currentNode1 == None and currentNode2 == None):
        currentNode.next = Node(0)
        if currentNode1 != None:
           currentNode.value += currentNode1.value
           currentNode1 = currentNode1.next
           
        if currentNode2 != None:
           currentNode.value += currentNode2.value
           currentNode2 = currentNode2.next
           
        if currentNode.value > 9:
           currentNode.value = currentNode.value%10
           currentNode.next.value = 1
           
        if currentNode1 == None and currentNode2 == None and currentNode.next.value == 0:           
           currentNode.next = None 
        else:
           currentNode = currentNode.next
        
    return result
    
number = NumberAsLinkedList(54321)
print(number)
print()

number1 = NumberAsLinkedList(99)
number2 = NumberAsLinkedList(25)
print(SumNumbers(number1,number2))


