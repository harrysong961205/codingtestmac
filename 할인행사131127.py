from collections import Counter
def solution(w, number, discount):
    answer = 0
    want = dict()
    for a in range(len(w)):
        want[w[a]] = number[a]
    
    for a in range(len(discount)-9):
        count = Counter(discount[a:a+10])
        inv_sum = 0
        #print("w ",want)
        #print("c ",count)
        for w in want:
            try:
                if want[w]-count[w] > 0:
                    inv_sum += want[w]-count[w]
            except:
                inv_sum += want[w]
                
        if inv_sum == 0:
            answer +=1
    return answer