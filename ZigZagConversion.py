'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows
'''

def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    orders = [''] * numRows
    for i in range(len(s)):
        if i // (numRows - 1) % 2 == 0:
            orders[i % (numRows - 1)] += s[i]
        else:
            orders[numRows - 1 - i % (numRows - 1)] += s[i]
    return ''.join(orders)

'''
Runtime: 60ms - 80.11%
Memory Usage: 13.6MB - 99.46%
'''