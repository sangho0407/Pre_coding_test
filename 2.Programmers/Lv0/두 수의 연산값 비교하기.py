def solution(a, b):
    mer = int(f"{a}{b}")
    mul = 2 * (a * b)
    if mer == mul :
        return mer
    return int(max(mer,mul))


# 한 수 배우는 코드

#def solution(a, b):
#    return max(int(str(a) + str(b)), 2 * a * b)