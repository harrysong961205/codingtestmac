
def solution(plans):
    # 잔업 함수
    def do_janup(c_time,n_time,wait_q,answer):
        rest_time = n_time - c_time
        print("janup",n_time, c_time,rest_time)
        # 남은시간 or wait_q가 비면 잔업 stop
        while rest_time !=0:
            if wait_q == []:
                break
            print("if or not")
            if wait_q[-1][0] <= rest_time:
                rest_time -= wait_q[-1][0]
                answer.append(wait_q.pop()[1])
                print(wait_q, "do again")
            else:
                wait_q[-1][0] -= rest_time
                print(c_time,wait_q, "do end")

                break



                    
            
    timeline = []
    wait_q = []
    answer = []
    # plans 시간순으로 정렬,timeline 생성
    for a in plans:
        poped = a.pop(1).split(":")
        a.insert(0,int(poped[0])*60 + int(poped[1]))
        a[2] = int(a[2])

    plans.sort()

    for a in plans:
        timeline.append(a[0])
        print(a)
    print("tl" ,timeline.pop(0))
    
    c_time = plans[0][0]

    #작업 시행
    for a in plans:
        if timeline == []:
            answer.append(a[1])
            break
        n_time = timeline.pop(0)
        if c_time + a[2] == n_time:
            answer.append(a[1])
            c_time = n_time
        elif c_time + a[2] < n_time:
            answer.append(a[1])
            c_time += a[2]
            if wait_q ==[]:
                c_time = n_time
            else:
                do_janup(c_time, n_time, wait_q, answer)
                c_time = n_time
        else:
            wait_q.append([c_time +a[2] - n_time,a[1]])
            c_time = n_time

    # timeline 다돌고 남은 작업들 최신순으로 answer append
    while wait_q != []:
        answer.append(wait_q.pop()[1])
    
    return answer

