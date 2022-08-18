import math
def solution(fees, records):
    def yogum(whole_time):
        if whole_time <= fees[0]:
            return fees[1]
        else:
            return (math.ceil((whole_time-fees[0])/fees[2]))*fees[3] + fees[1]
    answer = []
    cars = []
    for a in records:
        cars.append(a.split())
        cars[-1] = cars[-1][0].split(":"),cars[-1][1],cars[-1][2] 
    stack = []
    times = []
    whole_fee = []
    #print(cars)
    for a in cars:
        if a[2]== "IN":
            stack.append(a[1])
            times.append(a[0])
        else:
            now_out = stack.index(a[1])
            out_time = times.pop(now_out)
            h,m= int(a[0][0]) - int(out_time[0]), int(a[0][1]) - int((out_time[1]))
            whole_time = h*60 + m
            now_num = stack.pop(now_out)
            new = True
            for a in range(len(whole_fee)):
                if whole_fee[a][0] == now_num:
                    whole_fee[a][1] +=whole_time
                    new = False
                    break
            if new:
                whole_fee.append([now_num,whole_time])
                
    #print(whole_fee)
    #print(stack,times)
    
    if stack:
        for a in range(len(stack)):
            
            h,m = 23-int(times[a][0]),59-int(times[a][1])
            whole_time = h*60+m
            now_num = stack[a]
            new = True
            for a in range(len(whole_fee)):
                if whole_fee[a][0] == now_num:
                    whole_fee[a][1] +=whole_time
                    new = False
                    break
            if new:
                whole_fee.append([now_num,whole_time])
    #print(whole_fee)
    for a in sorted(whole_fee):
        answer.append(yogum(a[1]))

    return answer