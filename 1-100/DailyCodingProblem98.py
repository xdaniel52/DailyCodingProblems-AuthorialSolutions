"""
This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, 
exists(board, "SEE") returns true, 
exists(board, "ABCB") returns false
"""
def finder(board,word,row_id,col_id,g_path :list= []):

    if word == "":
        return True
    path = g_path.copy()
    path.append((row_id,col_id))
    if row_id > 0 and (row_id-1,col_id) not in path:
        if board[row_id-1][col_id] == word[0]:
            if finder(board,word[1:],row_id-1,col_id,path) == True:
                return True 
    if row_id < len(board)-1 and (row_id+1,col_id) not in path:
        if board[row_id+1][col_id] == word[0]:
            if finder(board,word[1:],row_id+1,col_id,path) == True:
                return True 
    if col_id > 0 and (row_id,col_id-1) not in path:
        if board[row_id][col_id-1] == word[0]:
            if finder(board,word[1:],row_id,col_id-1,path) == True:
                return True 
    if col_id < len(board[0])-1 and (row_id,col_id+1) not in path:
        if board[row_id][col_id+1] == word[0]:
            if finder(board,word[1:],row_id,col_id+1,path) == True:
                return True 

def exists(board,word):
    for row_id in range(len(board)):
        for col_id in range(len(board[0])):
            if board[row_id][col_id] == word[0]:
                if finder(board,word[1:],row_id,col_id) == True:
                    return True
    return False
                    

board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(exists(board, "ABCCED"))
print(exists(board, "SEE") )
print(exists(board, "ABCB")) 
