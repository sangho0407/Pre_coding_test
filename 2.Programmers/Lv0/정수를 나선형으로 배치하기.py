import numpy as np

def solution(n):
    arr = np.zeros((n, n), dtype=int)
    x, y = 0, 0  
    num = 1  

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    direction_idx = 0

    for _ in range(n * n):
        arr[x][y] = num
        num += 1

        next_x, next_y = x + directions[direction_idx][0], y + directions[direction_idx][1]

        if next_x < 0 or next_x >= n or next_y < 0 or next_y >= n or arr[next_x][next_y] != 0:
            direction_idx = (direction_idx + 1) % 4
            next_x, next_y = x + directions[direction_idx][0], y + directions[direction_idx][1]

        x, y = next_x, next_y

    return arr.tolist()
