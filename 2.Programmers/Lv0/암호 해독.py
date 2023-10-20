def solution(cipher, code):
    result = []
    for idx,char in enumerate(cipher):
        if (idx + 1) % code == 0 :
                result.append(char)
    return "".join(result)       
solution("dfjardstddetckdaccccdegk", 4)

# 한 수 배우는코드
'''
이렇게하면 더 파이써닉함 
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer

'''