def solution(w,h):
    if w==1 or h==1:
        answer = 0
    elif w==h:
        answer = (w-1)*h
        
    else:
        whole_area = w*h
        inv_area = 0
        for a in range(1,w+1):
            inv_area +=int(-h/w*a+h)
        answer = whole_area - (w*h-2*inv_area)

    return answer