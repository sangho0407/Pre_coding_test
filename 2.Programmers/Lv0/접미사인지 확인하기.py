def solution(my_string,is_suffix):
    answer = []   
    for i in range(len(my_string)) :
        answer.append(my_string[i:])
    if is_suffix in answer :
        return(1)
    else :
        return(0)
    
    
# 한 수 배우는 코드

'''

def solution(m, s):
    if m[-len(s):]==s: return 1
    return 0

'''