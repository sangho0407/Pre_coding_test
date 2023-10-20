agent = []
result = []

for _ in range(5):
    w = input()
    agent.append(w)

for i in range(5) :
    if 'FBI' in agent[i] :
        result.append(i+1)

for i in range(len(result)) :
    print(result[i],end=' ')

if not result :
    print ('HE GOT AWAY!')