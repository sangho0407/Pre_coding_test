def solution(my_string, alp):
    result = ''
    for idx,alps in enumerate(my_string) :
        if alps == alp :
            result += my_string[idx].upper()
            print(result)
        else :
            result += alps
    return result