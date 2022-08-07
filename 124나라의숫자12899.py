def jinbub(n):
    rev_base = ""
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    return rev_base[::-1]
def solution(n):
    answer = jinbub(n)
    while answer.count("0") != 0:
        #print(answer)
        answer = answer.replace("10","04")
        #print(answer)
        answer = answer.replace("20","14")
        #print(answer)
        answer = answer.replace("40","24")
        #print(answer)
        if answer[0] == "0": answer = answer[1:]
        #print("--------------------------")
        
        
    
    #while answer[0] =="0":
        #answer = answer[1:]
    #print("after:",answer)

    return answer