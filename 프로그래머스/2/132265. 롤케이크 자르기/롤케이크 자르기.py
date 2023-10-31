def solution(topping):
    answer = 0
    set1 = set()
    set2 = set()
    temp1 = [0] * (len(topping) - 1)
    temp2 = [0] * (len(topping) - 1)
    
    for i in range(len(topping) - 1):
        set1.add(topping[i])
        set2.add(topping[len(temp2) - i])
        
        temp1[i] = len(set1)
        temp2[len(temp2) - i - 1] = len(set2)

    for i in range(len(topping) - 1):
        if temp1[i] == temp2[i]:
            answer += 1
    
    return answer