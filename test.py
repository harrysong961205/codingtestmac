n = 7
k =3
e = [4, 2, 4, 5, 3, 3, 1]
import heapq
def solution(n, k, e):
    answer = 0
    heap = []
    round_num = 0
    while e:
        ene = e.pop(0)
        if n - ene>0:
            heapq.heappush(heap,-1 * ene)
        else:
            if n + -1*heapq.heappop(heap)>0 and k>0 :
                k-=1
            else:
                return round_num
        round_num +=1
    return round_num

print(solution(n,k,e))