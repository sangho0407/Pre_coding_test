n = int(input())

for j in range(1,n+1) :
    word = input()
    result = ''
    for i in range(len(word)) :
        temp = ord(word[i]) + 1
        if temp > 90 :
            temp = 65
        result += chr(temp)
    print('String #{}'.format(j))
    print(result)
    print()