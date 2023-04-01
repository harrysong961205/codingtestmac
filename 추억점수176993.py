def solution(name, yearning, photo):
    answer = []
    dict1 = {}
    # dict 화
    for a in zip(name,yearning):
        dict1[a[0]] = a[1]
    # 하나씩 꺼내면서 dict와 비교, 없는 사람 제외하고 다 더하기
    for b in photo:
        sum_pt = 0
        for c in b:
            if c in dict1:
                sum_pt += dict1[c]
        answer.append(sum_pt)
    return answer