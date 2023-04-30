from collections import Counter

def solution(w):
    answer = 0
    c = sorted(Counter(w).most_common(),reverse=True)
    while c:
        poped = c.pop()
        answer+=poped[1]*(poped[1]-1)/2
        for a in c:
            if poped[0]*1.5 == a[0]:
                answer += a[1]*poped[1]
            elif poped[0]*2 == a[0]:
                answer += a[1]*poped[1]
            elif poped[0]*4 == a[0]*3:
                answer += a[1]*poped[1]
        
    return answer