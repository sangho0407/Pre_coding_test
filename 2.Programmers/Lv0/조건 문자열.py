def solution(ineq, eq, n, m):
    result = str(n) + str(ineq) + eq + str(m)
    result = result.replace('!', '')
    return int(eval(result))


# 한 수 배우는 코드

'''
def solution(ineq, eq, n, m):
    return int(eval(str(n)+ineq+eq.replace('!', '')+str(m)))
'''