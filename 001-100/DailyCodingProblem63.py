"""
This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether 
the word can be found in the matrix by going left-to-right, or up-to-down.
"""

def find_word_in_matrix(matrix,word):
    word_len = len(word)   
    #checking rows       
    for col_id in range(len(matrix[0]) - word_len+1):     
        for row_id in range(len(matrix)):         
            for i in range(word_len):
                if not matrix[row_id][col_id+i] == word[i]:
                    break
            else:
                return True

    #checking columns
    for row_id in range(len(matrix) - word_len+1):      
        for col_id in range(len(matrix[0])):
            for i in range(word_len):
                if not matrix[row_id+i][col_id] == word[i]:
                    break
            else:
                return True
    return False


matrix =[['F', 'A', 'C', 'I'],
         ['O', 'B', 'Q', 'P'],
         ['A', 'N', 'O', 'B'],
         ['M', 'A', 'S', 'S']]

word = 'FOAM'
print(find_word_in_matrix(matrix,word))

word = 'MASS'
print(find_word_in_matrix(matrix,word))

word = 'IPBS'
print(find_word_in_matrix(matrix,word))

word = 'TEST'
print(find_word_in_matrix(matrix,word))






