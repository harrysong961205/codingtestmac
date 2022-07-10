def solution(arr):
    answer = 0
    if len(arr) ==1:
        return arr
    arr.sort()
    if arr[0] == 1:
        arr.pop(0)
    while len(arr)!=1:
        a = arr.pop(0)
        b = arr.pop(0)
        for i in range(max(a,b),a*b+1):
            if i%a==0 and i%b==0:
                arr.insert(0,i)
                break
    return arr[0]