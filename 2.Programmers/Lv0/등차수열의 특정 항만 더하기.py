def solution(a, d, included):
    sum_n = []
    sum_n.append(a)
    
    for i in range(len(included) - 1):
        sum_n.append(sum_n[i] + d)
    
    result_sum = 0  
    
    for idx, bools in enumerate(included):
        if bools:  
            result_sum += sum_n[idx]

    return result_sum
