def solution(food):
    answer = ''
    food.pop(0)
    cnt = 1
    while food:
        poped = food.pop(0)
        if poped != 1:
            answer+= str(cnt)*(poped//2)
        cnt+=1
    answer += "0" + answer[::-1]
    return answer