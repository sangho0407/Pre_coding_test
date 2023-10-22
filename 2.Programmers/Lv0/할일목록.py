def solution(todo_list, finished):
    answer = dict(zip(todo_list, finished))
    result = []
    for k, v in answer.items() :
        if v == False :
            result.append(k)
    return result