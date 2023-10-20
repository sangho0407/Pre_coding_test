def solution(my_string, m, c):
    # result: 전체 문자열을 m 글자씩 나눈 2차원 리스트 (문자열을 여러 줄로 나눈 것)
    # sublist: 현재 줄에 추가될 문자들을 임시로 저장하는 리스트
    # ans: 최종 결과를 저장하는 리스트 (세로로 읽은 글자들)
    result = []
    sublist = []
    ans = []

    # 문자열의 모든 글자를 순회하면서 
    for i in my_string:
        # 현재 글자를 sublist에 추가
        sublist.append(i)
        
        # sublist의 길이가 m과 같아지면
        if len(sublist) == m:
            # sublist를 result에 추가하고 sublist를 초기화
            result.append(sublist)
            sublist = []

    # 모든 줄에 대해서
    for j in result:
        # c번째 글자를 ans에 추가 (숫자는 0부터 시작하기 때문에 c-1)
        ans.append(j[c-1])

    # ans에 저장된 글자들을 연결하여 반환
    return ''.join(ans)
