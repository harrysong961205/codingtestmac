def solution(triangle):
    answer = 0
    stack = []
    for a in range(len(triangle)):
        if a == 0:
            continue
        for b in range(len(triangle[a])):
            if b == 0:
                triangle[a][b] += triangle[a-1][b]
            elif b == len(triangle[a])-1:
                triangle[a][b] += triangle[a-1][b-1]
            else:
                triangle[a][b] += max(triangle[a-1][b-1],triangle[a-1][b])
        #print(triangle)
    #print(triangle)
    return max(triangle[-1])