def solution(num_list):
    if num_list[-1] > num_list[-2]:
        num_list.append(num_list[-1] - num_list[-2])
    else: 
        num_list.append(num_list[-1]*2)
    return num_list


# 한 수 배우는 코드

'''

def solution(l):
    l.append(l[-1]-l[-2] if l[-1]>l[-2] else l[-1]*2)
    return l

'''