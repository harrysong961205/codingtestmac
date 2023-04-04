import collections
def solution(s):
    # 왼쪽에서 뺄꺼라 deque
    s = collections.deque(s)
    p_sum = [0]
    cnt = 1
    # 부분합 생성, 어짜피 -1,1,-1,1 .. 이나 1,-1,1,-1 .. 이나 abs먹여주면 똑같음
    while s:
        num = s.popleft()
        p_sum.append(p_sum[-1] + cnt*num)
        cnt = cnt * -1
    return abs(max(p_sum) - min(p_sum))