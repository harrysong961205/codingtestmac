def solution(wallpaper):
    answer = []
    X_s,X_e,Y,cnt = [],[],[],0
    
    for a in wallpaper:
        #try -> wallpaper의 n번째 줄에 #이 있을 경우, except -> #이 없는 경우
        try:
            # X_s : 시작 #의 idx, X_e : 끝 #의 idx, Y : Y좌표의 idx
            idx_s = a.index("#")
            print("index_s",idx_s)
            idx_e = len(a) - a[::-1].index("#")
            X_s.append(idx_s)
            X_e.append(idx_e)
            Y.append(cnt)
        except:
            pass
        cnt+=1
    # 줄 개념이 아닌 격자 개념이므로 max(Y) +1 해주기
    return [min(Y),min(X_s),max(Y)+1,max(X_e)]