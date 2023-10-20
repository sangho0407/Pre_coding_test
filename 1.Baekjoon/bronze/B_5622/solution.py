n = list(input())

alp = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

#결과값 초기화
cnt = 0

for i in n : # 입력값 n을 돌면서 
    for j in alp : # alp의 뭉터기를 하나씩 돌고
        if i in j : # 입력값 n의 한 요소가 j의 배열 안에 있으면 
            cnt += alp.index(j) + 3 # 초기화된 결과값 + alp의 인데스 요소에 +3

print(cnt)