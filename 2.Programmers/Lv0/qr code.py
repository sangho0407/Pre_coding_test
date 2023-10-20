def solution(q, r, code):
    answer = ''
    for i in range(len(code)) :
        if i % q == r :
            answer += code[i]
    return answer

#한 수 배우는 코드
'''

def solution(q, r, code):
    return code[r::q]

-- 코드 댓글

봐도 이해가 잘 안되긴함..

문자열 code의 index를 q로 나누면 q-1까지의 나머지가 q간격으로 반복되니 target 나머지가 곧 시작 index가 되고 그걸 code의 끝까지 q간격으로 반환하는거나 다름없습니다.
index = x * q + r 임을 알 수 있고, 우리가 필요한 index는 [0q+r, 1q+r, 2q+r... xq+r]입니다. 즉 [r, q+r, 2q+r... xq+r]임을 알 수있고, r로 시작해서 q씩 커지는 index만 가져오면 됩니다.


'''