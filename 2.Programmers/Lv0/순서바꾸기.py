def solution(num_list, n):
    slice_list = num_list[n:]
    rest_slice = num_list[:n]
    answer = slice_list + rest_slice
    return answer
