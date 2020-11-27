# '''
# Implement a basic calculator to evaluate a simple expression string.
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces.
# The integer division should truncate toward zero.
# '''

def calculate(s):
    def operate(op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        return a // b
    
    priorities = {
        '+': 0,
        '-': 0,
        '*': 1,
        '/': 1
    }

    result = 0
    nums = []
    ops = []
    current = ''
    for i in range(len(s)):
        if s[i].isdigit():
            current += s[i]
            if i == len(s) - 1:
                nums.append(int(current))
        else:
            if current != '':
                nums.append(int(current))
                current = ''
            if s[i] != ' ':
                while len(ops) > 0:
                    if priorities[s[i]] <= priorities[ops[-1]]:
                        result = operate(ops.pop(-1), nums.pop(-2), nums.pop(-1))
                        nums.append(result)
                    else:
                        break
                print(nums)
                ops.append(s[i])
    while len(ops) > 0:
        result = operate(ops.pop(-1), nums.pop(-2), nums.pop(-1))
        nums.append(result)
    return result

'''
Runtime: 80ms - 74.92%
Memory: 15.2MB - 93.71%
'''