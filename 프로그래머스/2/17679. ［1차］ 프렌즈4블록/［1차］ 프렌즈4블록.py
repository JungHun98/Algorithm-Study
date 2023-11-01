def find_block(board, temp_set, m, n):
    for i in range(m-1):
        for j in range(n-1):
            block = set([board[i][j], board[i][j+1], board[i+1][j], board[i+1][j+1]])
            
            if len(block) == 1:
                if '' not in block:
                    temp_set.add((i, j))
                    temp_set.add((i+1, j))
                    temp_set.add((i, j+1))
                    temp_set.add((i+1, j+1))

def down_block(board, m, n):
    for j in range(n):
        temp_str  = []
        for i in range(m):
            temp_str.append(board[i][j])
        
        down = ''.join(temp_str)
        next_ = m - len(down)
        
        for k in range(next_):
            board[k][j] = ''
            
        for c in down: 
            board[next_][j] = c
            next_ += 1

def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    
    while True:
        temp_set = set()
        find_block(board, temp_set, m, n)
        for x, y in temp_set:
            board[x][y] = ''
        down_block(board, m, n)

        if temp_set:
            answer += len(temp_set)
        else:
            break

    return answer