import collections
from collections import deque
def solution(s):
    dq = deque()
    for a in range(len(s)):
        dq.append(s[a])
        
        if len(dq) >=2:
            if dq[-1] == dq[-2]:
                
                dq.pop()
                dq.pop()
    if len(dq) == 0:
        return 1
    return 0
    #return answer