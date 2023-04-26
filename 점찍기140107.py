def solution(k, d):
    answer = 0
    if d<k:
        return 1
    a = 0
    while a <= d:
        #print("x :",a)
        #print("값 :", (d**2-a**2)**(1/2))
        #print("플러스 :",((d**2-a**2)**(1/2))//k +1)
        answer += ((d**2-a**2)**(1/2))//k +1
        a+=k
    return answer