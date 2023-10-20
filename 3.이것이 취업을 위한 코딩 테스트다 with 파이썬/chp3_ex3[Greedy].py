# n,m 공백으로 입력받기
n,m = map(int,input().split()) 

min_val = [] # 빈 리스트 대기

for _ in range(1,n+1) : # 한줄 씩 n번 입력받기
    x = list(map(int,input().split())) # 값 입력받기
    min_val.append(min(x)) # 각 행 마다 가장 작은 수 중 빈리스트에 추가

#각 행 마다 가장 작은 수 중 가장 큰 수 출력
print(max(min_val))