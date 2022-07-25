def solution(n, s):
    answer = []
    if s <n:
        return [-1]
    for a in range(n):
        answer.append(s//n)
    remain = s%n
    a=0
    while remain!=0:
        answer[a]+=1
        a+=1
        remain-=1
        