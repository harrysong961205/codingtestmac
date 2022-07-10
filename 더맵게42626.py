import heapq

def solution(scoville, K):
    mix_num = 0
    heapq.heapify(scoville)
    try:
        while scoville[0]<=K:
            scoville.append(heapq.heappop(scoville) + heapq.heappop(scoville)*2)
            mix_num += 1
    except IndexError:
            return -1
    return mix_num