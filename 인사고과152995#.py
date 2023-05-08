def solution(scores):
    if len(scores) ==1:
        return 1
    answer = 0
    eh = scores[0][:]
    s = sorted(scores,key=lambda x:(x[0],-x[1]))
    incentive = []
    while s:
        try:
            if s[-1][1]>s[-2][1]:
                poped = s.pop()
                s.pop()
                s.append(poped)
            else:
                incentive.append(s.pop())
        except:
            incentive.append(s[0])
            break
    if eh not in incentive:
        return -1
    rank = []
    for a in incentive:
        rank.append(a[0]+a[1])
    rank.sort(reverse=True)

    return rank.index(eh[0]+eh[1])+1