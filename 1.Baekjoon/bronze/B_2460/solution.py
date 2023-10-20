people = 0
on = []
for i in range(1,11) :
    a, b = map(int,input().split())
    people += b
    people -= a
    on.append(people)


print(max(on))