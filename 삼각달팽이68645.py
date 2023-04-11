from collections import deque
def solution(n):
    if n ==1:
        return [1]
    elif n ==2:
        return [1,2,3]
    elif n ==3:
        return [1,2,6,3,4,5]
    def do_next(whole_array,now_n):
        for a in range(len(whole_array)):
            whole_array[a] = deque([i+(3*(now_n-1)) for i in whole_array[a]])
            
        first = deque(list(range(2,now_n)))
        second = deque(list(range(now_n,2*now_n)))
        third = deque(list(range(2*now_n,3*now_n-2)))
        #print(second)
        third.reverse()
        #print(third)
        
        whole_array.appendleft(deque([]))
        
        for a in range(len(first)):
            whole_array[a].append(third[a])
            whole_array[a].appendleft(first[a])
            
        whole_array.appendleft(deque([1]))
        whole_array.append(second)
        
        return whole_array
    if n%3 == 0:
        first_one = deque([deque([1]),deque([2,6]),deque([3,4,5])])
        cnt =3
    elif n%3 == 2:
        first_one = deque([deque([1]),deque([2,3])])
        cnt =2
    else:
        first_one = deque([deque([1])])
        cnt =1
    answer = []
    while cnt != n:
        #print(cnt)
        cnt +=3
        answer = do_next(first_one,cnt)
    ans_dq = answer.popleft()
    for a in answer:
        ans_dq.extend(a)
    #print(list(ans_dq))
    return list(ans_dq)