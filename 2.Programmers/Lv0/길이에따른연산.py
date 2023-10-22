
from math import prod
def solution(num_list):
    answer = 0
    if len(num_list) >= 11 :
        answer = int(sum(num_list))
    else :
         answer = int(prod(num_list))
    return answer