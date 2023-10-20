def solution(code):
    result = ''
    mode = True
    for idx, ret in enumerate(code):
        if ret == "1":
            mode = not mode
        if mode == True and idx % 2 == 0:
            result += code[idx]
        elif mode == False and idx % 2 != 0:
            result += code[idx]
    result = result.replace('0', '')
    result = result.replace('1', '')
    if result == "":
        return "EMPTY"
    return result

# 한 수 배우는 코드

'''
def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"
'''