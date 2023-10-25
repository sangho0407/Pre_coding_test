import re

def solution(myStr):
    s = myStr
    answer = []
    for i in re.split('[abc]', s) :
        if i != "" :
            answer.append(i)
    if len(answer) == 0 :
        answer.append("EMPTY")
    return (answer)