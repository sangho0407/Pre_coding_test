mel = map(str,input().split())
ascending = '12345678'
descending = '87654321'
emtpy = ""
for i in mel :
    emtpy += i

if emtpy == ascending :
     print('ascending')
elif emtpy == descending :
    print('descending')
else :
    print('mixed')