'''
Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid.We define the validity of a string by these rules:
Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
'''

def checkValidString(self, s: str) -> bool:
    while s != s.replace("()", ""):
        s = s.replace("()", "")
        
    queue = []
    for i in range(len(s)):
        if s[i] in ["(", "*"]:
            queue.append(1)
        else:
            if queue:
                queue.pop()
            else:
                return False

    queue = []
    for i in range(len(s) - 1, -1, -1):
        if s[i] in [")", "*"]:
            queue.append(1)
        else:
            if queue:
                queue.pop()
            else:
                return False
    return True

'''
Runtime: 24ms - 93.29%
Memory: 14MB - 80.64%
'''