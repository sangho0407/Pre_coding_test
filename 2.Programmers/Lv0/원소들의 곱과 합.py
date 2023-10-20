def solution(num_list):
    mul = 1
    sum_sq = sum(num_list) ** 2
    for i in num_list :
        mul *= i
    if mul < sum_sq :
        return 1
    else : 
        return 0