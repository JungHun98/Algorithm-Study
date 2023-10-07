[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42747)

H-index 구하는 방법

어떤 과학자가 발표한 논문 `n`편 중, `h`번 이상 인용된 논문이 `h`편 이상이고 나머지 논문이 `h`번 이하 인용되었다면 `h`의 최댓값이 이 과학자의 H-Index입니다.

`Input`: 과학자가 발표한 논문의 인용 횟수를 담은 배열

`Output`: H-index

제한사항
- 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
- 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

배열의 길이는 최대 1000이므로 완전탐색으로 풀어도 괜찮을듯

1. 입력 배열을 정렬한다.
2. 배열을 index로 순회(0 ~ n-1)하면서 현재 인덱스의 배열 값(h), 현재 인덱스에서 부터 남은 배열의 길이를 비교한다.
3. 만약 현재 값이 남아있는 길이 값보다 크거나 같다면 `h`번 이상 인용된 논문이 `h`편 이상, 나머지 논문이 `h`번 이하 인용되었다는 조건을 만족 함. 
4. 배열을 모두 순회한다면 h-index는 0

(h-index는 citations에 포함된다는 보장이 없음)

```python
def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)

    for i in range(n):
        if citations[i] >= n - i:
            return n - i
        
    return answer
```