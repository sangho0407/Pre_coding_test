import numpy as np

def solution(my_string):
    num_str = np.arange(65,123) 
    ord_str = []
    result = []
    answer = []
    for i in my_string :
        ord_str.append(ord(i))
    for j in ord_str :
        if j not in num_str :
            result.append(chr(j))
    for k in result :
        answer.append(int(k))
    return (sum(answer))