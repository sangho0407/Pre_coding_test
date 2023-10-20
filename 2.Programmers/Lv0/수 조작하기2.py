def solution(numLog):
    result = ''
    for i in range(len(numLog) - 1):
        if numLog[i+1] - numLog[i] == 1:
            result += 'w'
        elif numLog[i+1] - numLog[i] == -1:
            result += 's'
        elif numLog[i+1] - numLog[i] == 10:
            result += 'd'
        elif numLog[i+1] - numLog[i] == -10:
            result += 'a'
        
    return result

#한 수 배우는 코드

'''

def solution(log):
    res=''
    joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
    return res

'''