def solution(m, n, puddles):
    answer = 0
    roads =[[0]*m for _ in range(n)]
    
            
    for a in range(n):
        for b in range(m):
            if [b+1,a+1] in puddles:
                continue
            try:
                up =roads[a-1][b]
            except:
                up =0
            try:
                left = roads[a][b-1]
            except:
                left = 0
            
            roads[a][b] = roads[a-1][b] + roads[a][b-1]
            if a==0 and b ==0:
                
                roads[0][0] =1
        
    for a in roads:
        print(a)
    return roads[n-1][m-1]%1000000007