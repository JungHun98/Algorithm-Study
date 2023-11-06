def solution(numbers):
    answer = []
    
    for n in numbers:
        b_list = list(bin(n)[2:])
        idx = bin(n)[2:].rfind('0')
        
        if idx > -1:
            b_list[idx] = '1'
            if idx < len(b_list) - 1:
                b_list[idx+1] = '0'
        else:
            b_list = ['1'] + b_list
            b_list[1] = '0'
    
        answer.append(int(''.join(b_list),2))
    
    return answer