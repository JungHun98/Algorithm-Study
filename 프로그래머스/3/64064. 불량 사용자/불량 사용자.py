from itertools import permutations

def is_mappting(source, target):
    if len(source) != len(target):
        return False
    
    for i in range(len(target)):
        if target[i] == '*' or target[i] == source[i]:
            continue
        else:
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    temp_result = []
    temp_list = list(permutations(user_id, len(banned_id)))

    for temp in temp_list:
        result = True

        for i in range(len(banned_id)):
            if not is_mappting(temp[i], banned_id[i]):
                result = False
                break
        
        if result:
            s = set(temp)
            if s not in temp_result:
                temp_result.append(s)
                answer += 1
    
    return answer