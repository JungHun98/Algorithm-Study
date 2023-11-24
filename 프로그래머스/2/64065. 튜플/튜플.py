def solution(s):
    answer = []
    number_hash = {}
    
    set_string_list = s[2:-2].split('},{')
    
    for set_string in set_string_list:
        for number in set_string.split(','):
            if number in number_hash:
                number_hash[number] += 1
            else:
                number_hash[number] = 1
            
    sorted_hash = sorted(number_hash.items(), reverse=True, key=lambda x: x[1])
    
    for key, value in sorted_hash:
        answer.append(int(key))
    
    return answer