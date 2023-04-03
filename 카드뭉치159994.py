def solution(cards1, cards2, goal):
    answer = ''
    # pop(0) 하다보면 card1이 빈 리스트여서 오류 남. 이상한 값 집어넣기
    cards1.append("!@#")
    cards2.append("!@#")
    while goal:
        current_word = goal.pop(0)
        #cards1 비교
        if current_word == cards1[0]:
            cards1.pop(0)
            continue
        #cards2 비교
        if current_word == cards2[0]:
            cards2.pop(0)
            continue
        # 둘다 안되면 no
        return "No"
    # 끝까지 가면 Yes
    return "Yes"