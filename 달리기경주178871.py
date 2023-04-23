import collections
def solution(players, c):
    ans = []
    answer = []
    c = collections.deque(c)
    dict_nm = {}
    dict_rk = {}

    for a in enumerate(players):
        dict_nm[a[1]]=a[0]
        dict_rk[a[0]]=a[1]
    #print(dict_nm)
    #print(dict_rk)

    while c:
        poped = c.popleft()
        rank = dict_nm[poped]
        front = dict_rk[rank-1]
        
        dict_nm[front] += 1
        dict_nm[poped] -=1
        
        dict_rk[rank] = front
        dict_rk[rank-1] = poped
    #print(dict_nm)
    #print(dict_rk)
    answer = []
    for a in dict_rk:
        answer.append(dict_rk[a])
    return answer