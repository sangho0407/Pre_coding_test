def solution(myString):
    answer = []
    my_string = myString.split('x')
    for i in my_string :
        if i != "" :
            answer.append(i)
    return sorted(answer)