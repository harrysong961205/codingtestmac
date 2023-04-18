def solution(t, p):
    answer = 0
    goal = int(p)
    w = len(p)
    while len(t)>=w:
        if int(t[:w]) <=goal:
            answer +=1
        t = t[1:]
    return answer