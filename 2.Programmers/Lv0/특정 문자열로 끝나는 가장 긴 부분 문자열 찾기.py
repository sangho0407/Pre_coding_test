def solution(myString, pat):
    slice_str = myString.rfind(pat)
    return myString[:slice_str+len(pat)]