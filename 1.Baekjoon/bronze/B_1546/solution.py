# 첫째줄에 시험과목 n 개를 입력받고, n개의 현재 성적을 입력받는다
# 입력받은 현재성적을 하나씩 현재성적/최대성적*100 을 해서 새로운 성적의 평균값을 구한다.


empty = []
result= []

n = int(input())
current = list(map(int,input().split()))
for i in current :
    empty.append(i)

for i in empty :
    result.append(i/max(empty)*100)

print(sum(result)/len(result))