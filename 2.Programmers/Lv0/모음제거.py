def solution(my_string):
    answer = ''
    gather = ["a","e","i","o" ,"u" ]
    for i in my_string :
        if i not in gather :
            answer += i
    return (answer)