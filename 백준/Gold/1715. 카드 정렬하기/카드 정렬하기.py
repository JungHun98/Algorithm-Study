import heapq

def solution(cards):
    answer = 0
    heapq.heapify(cards)
    while len(cards) > 1:
        first = heapq.heappop(cards)
        second = heapq.heappop(cards)
        sum_ = first + second
        answer += sum_
        heapq.heappush(cards, sum_)

    return answer

N = int(input())
cards = []

for _ in range(N):
    cards.append(int(input()))

print(solution(cards))
