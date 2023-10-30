def solution(board, k):
    total_sum = 0
    
    rows = len(board)
    
    for i in range(rows):
        for j in range(len(board[i])):
            if i + j <= k:
                total_sum += board[i][j]
    
    return total_sum