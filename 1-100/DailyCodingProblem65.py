"""
This problem was asked by Amazon.

Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.
"""

def PrintClockwise(matrix):
    if len(matrix) > len(matrix[0]):
        iterations = len(matrix[0])*2
    else:
        iterations =len(matrix)*2-1
 
    row_id = 0
    col_id = 0
    top_border = 0
    bottom_border = len(matrix)-1
    left_border = 0
    rigth_border = len(matrix[0])-1
    print(matrix[0][0])
    for i in range(iterations):
        if i%4 == 0:
            while col_id < rigth_border:
                col_id+=1
                print(matrix[row_id][col_id])             
            top_border+=1
                
        elif i%4 == 1:
            while row_id < bottom_border:
                row_id+=1
                print(matrix[row_id][col_id])              
            rigth_border-=1
            
        elif i%4 == 2:
            while col_id > left_border:
                col_id-=1
                print(matrix[row_id][col_id])               
            bottom_border-=1
        else:
            while row_id > top_border:
                row_id-=1
                print(matrix[row_id][col_id])           
            left_border+=1
        

matrix =[[1,  2,  3,  4,  5],
         [6,  7,  8,  9,  10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20]]

PrintClockwise(matrix)