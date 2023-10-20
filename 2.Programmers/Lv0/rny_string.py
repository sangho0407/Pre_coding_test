def solution(rny_string):
    answer = ''
    for str in rny_string :
        if str == 'm' :
            str = 'rn'
        answer += str
    return answer



'''
def solution(rny_string):
    return rny_string.replace('m', 'rn') # 띵작: 'rnasterpiece'
'''