import collections
def solution(targets):
    targets = sorted(targets, key = lambda x:x[1])
    targets = collections.deque(targets)
    bef = targets.popleft()
    cnt =1
    while targets:
        poped = targets.popleft()
        if poped[0]<bef[1]:
            #print(poped,bef)
            pass
        else:
            cnt+=1
            #print(poped,bef, "change")
            bef = poped
    return cnt