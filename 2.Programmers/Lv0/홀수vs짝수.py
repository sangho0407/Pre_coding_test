def solution(num_list):
    even = []
    odd = []
    for i in range(len(num_list)):
        if i % 2 == 0 :
            even.append(num_list[i])
        else :
            odd.append(num_list[i])
    return max(sum(even),sum(odd))