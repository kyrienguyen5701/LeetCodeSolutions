'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using
the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6"
is different from "06".
In addition to the mapping above, an encoded message may contain the '*' character,
which can represent any digit from '1' to '9' ('0' is excluded).
For example, the encoded message "1*" may represent any of the encoded messages
"11", "12", "13", "14", "15", "16", "17", "18", or "19".
Decoding "1*" is equivalent to decoding any of the encoded messages it can represent.
Given a string s containing digits and the '*' character, return the number of ways to decode it.
Since the answer may be very large, return it modulo 109 + 7.
'''

from collections import deque

def numDecodings(s):
    if s[0] == '0':
        return 0
    mod = 1000000007
    dp = deque([9 if s[0] == '*' else 1])
    if len(s) == 1:
        return dp[0]
    if '*' not in s[:2]:
        if s[1] == '0':
            if int(s[0]) < 3:
                dp.append(1)
            else:
                return 0
        else:
            dp.append(2 if int(s[:2]) < 27 else 1)
    else:
        if s[:2] == '**':
            dp.append(96)
        else:
            if s[0] == '*':
                if s[1] == '0':
                    dp.append(2)
                elif int(s[1]) < 7:
                    dp.append(11)
                else:
                    dp.append(10)
            if s[1] == '*':
                if s[0] == '1':
                    dp.append(18)
                elif s[0] == '2':
                    dp.append(15)
                else:
                    dp.append(9)
    for i in range(2, len(s)):
        prev, curr = s[i - 1], s[i]
        if curr == '0':
            if prev not in ('1', '2', '*'):
                return 0
            else:
                dp.append(dp.popleft() * 2 % mod if prev == '*' else dp.popleft())
        else:
            c0 = 0
            c1 = 9 if curr == '*' else 1
            if prev == '1':
                c0 = 9 if curr == '*' else 1
            elif prev == '2':
                if curr == '*':
                    c0 = 6
                else:
                    c0 = 1 if int(curr) < 7 else 0
            elif prev == '*':
                if curr != '*':
                    c0 = 2 if int(curr) < 7 else 1
                else:
                    c0 = 15
            dp.append((dp.popleft() * c0 + dp[-1] * c1) % mod)
    return dp[1]

'''
Runtime: 200ms - 98.59%
Memory Usage: 15MB - 95.76% 
'''

'''
Comment: Similar idea to the Count Vowels Permutation
'''