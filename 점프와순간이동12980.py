def solution(n):
    
    cnt = 0
    while n!=1:
        if n%2 ==0:
            n = n/2
        else:
            n -=1
            cnt +=1
    

    return cnt+1