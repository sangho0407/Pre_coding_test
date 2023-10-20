def solution(n):
    answer = []
    answer.append(n)
    for i in range(n) :
        if answer[i] == 1 :
            break
        if answer[i] % 2 == 0 :
            answer.append(int(answer[i]/2))
        else : 
            answer.append(int((3 * answer[i]) + 1))

    return answer


# 한 수 배우는 코드

'''
# while문을 쓰면 되는데 맨날 for만 돌려서 까먹음..

def solution(n):
    answer = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        answer.append(n)
    return answer
'''