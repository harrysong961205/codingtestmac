from itertools import product
def solution(users, emoticons):
    answer = []
    cases = []
    es = len(emoticons)
    for user in users:
        user[0] = 1-user[0]/100

    rates = list(product([10,20,30,40],repeat=es))
    
    for r in rates:
        inv_row = []
        for num in range(len(emoticons)):
            inv_row.append((emoticons[num],1-r[num]/100))
        cases.append(inv_row)
        
    for case in cases:
        user_sum = [0,0]
        for user in users:
            inv_sum = [0,0]

            case_sum = 0
            for a in case:
                if a[1] <=user[0]:
                    case_sum+=a[0]*a[1]
            if case_sum >= user[1]:
                inv_sum[0]+=1
            else:
                inv_sum[1]+=case_sum
            user_sum[0]+=inv_sum[0]
            user_sum[1]+=inv_sum[1]
            
        answer.append(user_sum)
        
                
    ans = sorted(answer,key=lambda x:(-x[0],-x[1]))[0]
    ans[1] = int(ans[1])
        
    return ans