def solution(my_strings, parts):
    result = []
    for idx in range(len(parts)):
        i,j = parts[idx]
        result.append(my_strings[idx][i:j+1])
    return ''.join(result)


# 한 수 배우는 코드

'''
enumerate를 이렇게도 사용이 가능 하구나..

def solution(my_strings, parts):
    answer = ""
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]
    return answer
    
'''