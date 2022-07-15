def solution(record):
    answer = []
    stc_list = {}
    for a in record:
        a = a.split()
        if a[0] =="Change" or a[0] == "Enter":
            stc_list[a[1]]=a[2]
    for a in record:
        a = a.split()
        if a[0] == "Enter":
            answer.append(f"{stc_list[a[1]]}님이 들어왔습니다.")
        elif a[0] == "Leave":
             answer.append(f"{stc_list[a[1]]}님이 나갔습니다.")
            

    

    
    return answer