def solution(s):
    answer = []
    s = list(s)
    pool = set([])
    idx = {}
    cnt = 0
    while s:
        ext_num = s.pop(0)
        if ext_num in pool:
            answer.append(cnt-idx[ext_num])
        else:
            answer.append(-1)
        idx[ext_num] = cnt
        pool.add(ext_num)
        cnt+=1
    return answer