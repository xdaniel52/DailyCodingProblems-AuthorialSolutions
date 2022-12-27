"""
This problem was asked by Dropbox.

Spreadsheets often use this alphabetical encoding for its columns: 
    "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. 
For example, given 1, return "A". Given 27, return "AA".
"""

def column_name(col_number):
    name = ""
    col_number-=1
    n = col_number%26
    col_number=(col_number - n)  // 26
    
    if col_number > 0:
        name+=column_name(col_number)
    return name+chr(65 + n) 



print(column_name(1))

print(column_name(26))
print(column_name(27))
print(column_name(28))
