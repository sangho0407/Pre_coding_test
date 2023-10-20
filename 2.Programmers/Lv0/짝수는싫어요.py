def solution(n):
    answer = []
    for i in range(1,n+1) :
        answer.append(i)
    for idx,num in enumerate(answer) :
        if num % 2 == 0 :
            del(answer[idx])
    return answer