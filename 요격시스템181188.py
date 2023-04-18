import collections
def solution(targets):
    targets = sorted(targets, key = lambda x:x[1])
    targets = collections.deque(targets)
    bef = targets.popleft()
    cnt =1
    while targets:
        poped = targets.popleft()
        if poped[0]<bef[1]:
            pass
        else:
            cnt+=1
            bef = poped
    return cnt