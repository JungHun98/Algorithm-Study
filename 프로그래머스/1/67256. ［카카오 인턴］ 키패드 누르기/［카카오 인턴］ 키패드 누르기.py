def solution(numbers, hand):
    answer = ''
    pos_dic = {}
    pos_dic[0] = (3,1)
    
    for i in range(3):
        for j in range(3):
            pos_dic[i * 3 + j + 1] = (i, j)

    left_pos = (3, 0)
    right_pos = (3, 2)
    
    for num in numbers:
        next_hand = ''
        if (num - 1) % 3 == 0:
            next_hand = 'L'
        elif num > 0 and num % 3 == 0:
            next_hand = 'R'
        else:
            pos = pos_dic[num]
            left_len = abs(left_pos[0] - pos[0]) + abs(left_pos[1] - pos[1])
            right_len = abs(right_pos[0] - pos[0]) + abs(right_pos[1] - pos[1])
            
            if left_len < right_len:
                next_hand = 'L'
            elif left_len > right_len:
                next_hand = 'R'
            else:
                if hand == 'left':
                    next_hand = 'L'
                else:
                    next_hand = 'R'
        
        if next_hand == 'L':
            left_pos = pos_dic[num]
        else:
            right_pos = pos_dic[num]
            
        answer += next_hand
    return answer