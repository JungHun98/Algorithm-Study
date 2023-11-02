from collections import deque 

def solution(x, y, n):
    answer = 0
    queue = deque([y])
    if x == y:
        return 0
    
    while queue:
        next_list = list(queue)
        next_queue = deque()
        answer += 1
        
        for num in next_list:
            new_list = [num - n]
            
            if num % 2 == 0:
                new_list.append(num // 2)
            if num % 3 == 0:
                new_list.append(num // 3)
                
            for temp in new_list:
                if temp >= x:
                    if temp == x:
                        return answer
                    else:
                        next_queue.append(temp)
            
        queue = next_queue
        
    return -1