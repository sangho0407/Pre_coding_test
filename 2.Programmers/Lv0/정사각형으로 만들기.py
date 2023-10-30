def solution(arr):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    
    if rows > cols:
        for row in arr:
            row.extend([0] * (rows - cols))
        return arr
    

    elif cols > rows:
        for _ in range(cols - rows):
            arr.append([0] * cols)
        return arr
    
    else:
        return arr

