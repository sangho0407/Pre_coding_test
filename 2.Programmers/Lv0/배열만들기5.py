def solution(intStrs, k, s, l):
    answer = []
    for idx,num in enumerate(intStrs) :
        if k < int(intStrs[idx][s:s+l]) :
            answer.append(int(intStrs[idx][s:s+l]))
    return answer    

'''
# 굳이 enumerate쓸 필요가 없었음 ㅋ
def solution(intStrs, k, s, l):
    answer = []
    for x in intStrs:
        if int(x[s:s+l])>k:answer.append(int(x[s:s+l]))
    return answer
'''