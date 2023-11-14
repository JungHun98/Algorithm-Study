from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue_1 = deque(queue1)
    queue_2 = deque(queue2)
    
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    while True:
        if sum1 == sum2:
            return answer
        if len(queue_1) == 0 or len(queue_2) == 0:
            return -1
        
        if sum1 > sum2:
            pop = queue_1.popleft()
            sum1 -= pop
            sum2 += pop
            queue_2.append(pop)
        else:
            pop = queue_2.popleft()
            sum2 -= pop
            sum1 += pop
            queue_1.append(pop)
        
        answer += 1
        
        if answer > len(queue1) * 4:
            return -1
        
    return answer