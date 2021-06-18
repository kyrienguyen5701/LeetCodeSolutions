'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

def generateParenthesis(n):
    result = []
    def backtracking(nOpen, nClose, path):
        if nClose == n:
            result.append(path)
            return
        if nOpen < n:
            backtracking(nOpen + 1, nClose, path + '(')
        if nClose < nOpen:
            backtracking(nOpen, nClose + 1, path + ')')
    backtracking(0, 0, '')
    return result

'''
Runtime: 32ms - 85.47%
Memory Usage: 14.3MB - 96.06%
'''