"""
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether 
the word can be found in the matrix by going left-to-right, or up-to-down.
"""

def FindWordInMatrix(matrix,word):
    wordLen = len(word)   
    #checking rows       
    for colID in range(len(matrix[0]) - wordLen+1):     
        for rowID in range(len(matrix)):         
            for i in range(wordLen):
                if not matrix[rowID][colID+i] == word[i]:
                    break
            else:
                return True

    #checking columns
    for rowID in range(len(matrix) - wordLen+1):      
        for colID in range(len(matrix[0])):
            for i in range(wordLen):
                if not matrix[rowID+i][colID] == word[i]:
                    break
            else:
                return True
    return False


matrix =[['F', 'A', 'C', 'I'],
         ['O', 'B', 'Q', 'P'],
         ['A', 'N', 'O', 'B'],
         ['M', 'A', 'S', 'S']]

word = 'FOAM'
print(FindWordInMatrix(matrix,word))

word = 'MASS'
print(FindWordInMatrix(matrix,word))

word = 'IPBS'
print(FindWordInMatrix(matrix,word))

word = 'TEST'
print(FindWordInMatrix(matrix,word))






