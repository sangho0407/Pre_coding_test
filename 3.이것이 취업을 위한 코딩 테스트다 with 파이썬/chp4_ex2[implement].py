point = str(input())
row = int(point[1])
col = ord(point[0])

step = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

cnt = 0

for i in step :
    x = row + i[0]
    y = col + i[1]
    if 1<= x <= 8 and 97<= y <=104 :
        cnt += 1
print(cnt)
