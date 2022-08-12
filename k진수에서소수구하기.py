import math
def jinbub(n,k):
    if k == 10:
        return str(n)
    rev_base = ""
    while n>0:
        n,mod = divmod(n,k)
        rev_base+= str(mod)
    return rev_base[::-1]
def sosu(n):
    if n ==1:
        return False
    else:
        for a in range(2,int(n**(1/2))+1):
            if n%a==0:
                return False
        return True
def solution(n, k):
    answer = -1
    cnt = 0
    for i in jinbub(n,k).split("0"):
        if i =="":
            continue
        else:
            if sosu(int(i)):
                cnt +=1
    print(int(3.7))
    return cnt
    print(int)
    return answer