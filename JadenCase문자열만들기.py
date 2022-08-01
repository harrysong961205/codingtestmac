def solution(s):
    if len(s) == 1:
        return s.upper()
    answer = ''
    answer += s[0].upper()
    for a in range(1,len(s)):
        if s[a-1] == " ":
            now = s[a].upper()
            answer += now
        else:
            now = s[a].lower()
            answer += now
    if s[-2] ==" ":
        answer += s[-1].upper()
    else:
        answer += s[-1]
    
    return answer[:len(answer)-1]