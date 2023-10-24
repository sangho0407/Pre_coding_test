def solution(myString):
    answer = []
    my_string = myString.split('x')
    for i in my_string :
        answer.append(len(i))
    return (answer)