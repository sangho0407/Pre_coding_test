def solution(strArr):
    lengths_count = [0] * 31  
    
    for s in strArr:
        lengths_count[len(s)] += 1
        
    return max(lengths_count)