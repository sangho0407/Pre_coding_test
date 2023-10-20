def solution(arr, idx):
    for i in range(len(arr)):  # 전체 원소를 확인
        if i >= idx and arr[i] == 1:  # i가 idx보다 크거나 같고, arr[i]가 1인 경우
            return i  # 조건에 맞는 인덱스 반환
    return -1  # 조건에 맞는 인덱스를 찾지 못한 경우



# 한 수 배우는 코드

'''


def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer

'''