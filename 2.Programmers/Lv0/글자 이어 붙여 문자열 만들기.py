def solution(my_string, index_list):
    answer = ''
    for i in index_list :
        answer += my_string[i]
    return answer

# 한 수 배우는 코드
''''

def solution(my_string, index_list):
    return ''.join([my_string[idx] for idx in index_list])


def solution(my_string, index_list):
    return ''.join(map(lambda x: my_string[x], index_list))

'''