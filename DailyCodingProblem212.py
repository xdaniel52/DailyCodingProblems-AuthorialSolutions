"""
This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: 
    "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. 
For example, given 1, return "A". Given 27, return "AA".
"""

def ColumnName(colNumber):
    name = ""
    colNumber-=1
    n = colNumber%26
    colNumber=(colNumber - n)  // 26
    
    if colNumber > 0:
        name+=ColumnName(colNumber)
    return name+chr(65 + n) 



print(ColumnName(1))
print(ColumnName(27))

#for i in range(1,27*26+2 ):
#   print(ColumnName(i))