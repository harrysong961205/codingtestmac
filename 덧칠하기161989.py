def solution(n, m, s):
    # 브러쉬 크기가 1이면 어짜피 다 칠해야함
    if m ==1:
        return len(s)
    answer = 0
    # 브러쉬가 자기 자신 포함 칠하기니까 -1 해주기
    while s:
        num = s.pop()
        answer +=1
        try:
            while s[-1] >= num -(m-1):
                s.pop()
        except:
            break
            
    return answer