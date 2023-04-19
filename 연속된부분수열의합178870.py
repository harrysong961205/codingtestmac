def solution(sequence, k):
    answer = []
    while True:
        if sequence[-1]>k:
            sequence.pop()
        else:
            break
    s_origin = sequence[:]

    inv_sum = 0
    inv = []
    loc = [len(sequence)-1,len(sequence)-1]
    inv_sum += sequence.pop()
    #print(loc)
    #s_origin = sequence[:]
    while sequence:
        #print("inv_sum", inv_sum, loc)
        if inv_sum < k:
            inv_sum += sequence.pop()
            loc[0] -= 1
        elif inv_sum == k:
            inv.append([loc[:][0],loc[:][1]])
            #print("loc 삽입",loc)
            inv_sum -= s_origin[loc[1]]
            loc[1] -= 1
        else:
            #print("index",loc[1],"value",s_origin[loc[1]],"제거")
            inv_sum -= s_origin[loc[1]]
            loc[1] -= 1
            #print("inv_sum", inv_sum, loc)

    if inv_sum == k:
        inv.append([loc[:][0],loc[:][1]])
        #print("loc 삽입",loc)

    inv = sorted(inv, key=lambda x:(x[1]-x[0],x))
    return inv[0]