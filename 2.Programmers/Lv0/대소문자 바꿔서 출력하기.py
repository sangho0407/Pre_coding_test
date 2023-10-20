str = input()
emp = []
if 1 <= len(str) <= 20 :
    str = list(str)
    for alp in str :
        if 65 <= ord(alp) <= 90 :
            emp.append(alp.lower())
        if 97 <= ord(alp) <= 122 :
            emp.append(alp.upper())
result = ''.join(s for s in emp)
print(result)

# 한수 배우는 다른 코드 ... 
# print(input().swapcase())