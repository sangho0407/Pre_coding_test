while True :
    a, b = input().strip().split(' ')
    
    if 1 <= len(a) <= 10 and 1 <= int(b) <= 5 :
        a = a
        b = b
        print(a * int(b))
        break
    else :
        print('컨디션 확인')
        continue
