def solution(my_string):
    answer = []

    for i in range(65, 90 + 1):  
        answer.append(my_string.count(chr(i)))

    for i in range(97, 122 + 1): 
        answer.append(my_string.count(chr(i)))

    return answer