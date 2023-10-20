def solution(l, r):
    result = []

    for i in range(l, r + 1):
        num_str = str(i)
        is_valid = True

        for char in num_str:
            if char != '0' and char != '5':
                is_valid = False
                break

        if is_valid:
            result.append(i)

    if result:
        return result
    else:
        return [-1]
    