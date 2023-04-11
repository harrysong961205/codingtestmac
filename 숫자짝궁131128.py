from collections import Counter
def solution(X, Y):
    answer = ''
    X,Y = dict(Counter(X)),Counter(Y)
    for a in "0123456789":
        try:
            answer += str(a) * min(X[a],Y[a])
        except:
            pass
    if answer == "":
        return "-1"
    
    elif set(answer) == {'0'}:
        return "0"
    return answer[::-1]