import heapq

def solution(scoville, K):
    # scoville 리스트를 최소 힙으로 변환
    heapq.heapify(scoville)
    # 섞은 횟수를 저장할 변수 초기화
    answer = 0

    # 힙의 크기가 1보다 크고, 힙의 최소값이 K 미만인 동안 반복
    while len(scoville) > 1 and scoville[0] < K:
        # 가장 맵지 않은 음식과 두 번째로 맵지 않은 음식을 가져옴
        least_spicy = heapq.heappop(scoville)
        second_least_spicy = heapq.heappop(scoville)
        # 두 음식을 섞어 새로운 음식 생성
        mixed_spicy = least_spicy + (second_least_spicy * 2)
        # 새로운 음식을 힙에 추가
        heapq.heappush(scoville, mixed_spicy)
        # 섞은 횟수 증가
        answer += 1

    # 모든 음식의 스코빌 지수가 K 이상이면 섞은 횟수 반환, 그렇지 않으면 -1 반환
    return answer if scoville[0] >= K else -1

# 함수를 테스트
result = solution([1, 2, 3, 9, 10, 12], 7)
print(result)  # 출력: 2
