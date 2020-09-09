'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
You may assume the default revision number for each level of a version number to be 0. 
For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0
'''

def compareVersion(v1, v2):
    p1,p2=0,0
    v1l=v1.split('.')
    v2l=v2.split('.')
    
    while p1<len(v1l) and p2<len(v2l):
        
        if int(v1l[p1])>int(v2l[p2]):
            return 1
        if int(v1l[p1])<int(v2l[p2]):
            return -1
        p1+=1
        p2+=1
        
    if len(v1l)==len(v2l):
        return 0
    if p1==len(v1l): 
        while p2<len(v2l):
            if int(v2l[p2])>0:
                return -1
            p2+=1
        return 0
    if p2==len(v2l): 
        while p1<len(v1l):
            if int(v1l[p1])>0:
                return 1
            p1+=1
        return 0

print(compareVersion('01', '1'))
'''
Runtime: 24ms - 94.61%
Memory: 13.6MB - 94.94%
'''