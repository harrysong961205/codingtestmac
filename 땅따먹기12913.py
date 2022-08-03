def solution(land):
    answer = 0
    now = land.pop(0)
    for a in land:
        for b in range(len(now)):
            line = now.copy()
            line.pop(b)
            a[b] += max(line)
        now = a.copy()
    
            
    return max(now)