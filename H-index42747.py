def solution(citations):
    answer = 0
    citations.sort()
    H_index = []
    for a in range(1,len(citations)+1):
        min_list = []
        max_list = []
        for b in citations:
            if a <= b:
                max_list.append(b)
            
        #print(min_list,max_list, a)
        if len(max_list)>= a:
            H_index.append(a)
            
    
    if H_index == []:
        return 0
    return max(H_index)