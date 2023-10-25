def solution(order):
    order = list(map(int, str(order)))
    answer = 0
    for i in order:
        if i != 0 and i % 3 == 0:  
            answer += 1
    return answer

# 한 수 배우는 코드
'''
def solution(order):
    answer = 0
    order = str(order)
    return order.count('3') + order.count('6') + order.count('9')
    
def solution(order):
    return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))
'''