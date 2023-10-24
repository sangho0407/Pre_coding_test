def solution(myString, pat):
    switch = ''
    for i in myString :
        if i == 'A' :
            switch += 'B'
        else :
            switch += "A"
    return 1 if pat in switch else 0