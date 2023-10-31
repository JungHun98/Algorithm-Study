T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    sales = list(map(int, input().split()))
    sales.reverse()
    result = 0
    prev = sales[0]
    
    for val in sales:
        if val > prev:
            prev = val
        else:
            result += (prev - val)
    
    print(f'#{test_case} {result}')
    # ///////////////////////////////////////////////////////////////////////////////////
