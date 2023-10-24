def solution(my_string):
    answer = []
    result = []
    my_string = my_string.split(' ')
    for i in my_string :
        if "" != i :
            result.append(i)
    return result