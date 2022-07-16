import collections
from collections import deque
def solution(priorities, location):
    answer = []
    done =[]
    pl = deque([])
    dq = priorities
    for a in range(len(priorities)):
        pl.append([dq[a],a])
    #print(pl)
    cnt =0
    while len(pl) != 0:
        printpr = []
        for a in range(len(pl)):
            printpr.append(pl[a][0])
        printpr.sort(reverse=True)
        #print(printpr)
        now_pr=pl.popleft()
        if now_pr[0]>=printpr[0]:
            answer.append(now_pr)
            #print("answer append:", now_pr)
        else:
            pl.append(now_pr)
           # print("pl append:", now_pr)
       # print(pl)
    print(answer)
    for a in range(len(answer)):
        
        if answer[a][1] == location:
            
            return a+1