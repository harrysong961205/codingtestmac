import collections
def solution(k, m, score):
    cnt = 0
    s = sorted(score,reverse = True)
    s = collections.deque(s)
    answer = []
    while s:
        inv = []
        for a in range(m):
            try:
                inv.append(s.popleft())
            except:
                inv = [0]
                break
        answer.append(inv)
    while answer:
        r = answer.pop()
        cnt += min(r)*len(r)
        
    return cnt