def solution(my_string):
    total_sum = 0
    num_str = ''  
    
    for char in my_string:
        if char.isdigit():  
            num_str += char  
        elif num_str:  
            total_sum += int(num_str)  
            num_str = '' 
    
    if num_str:  
        total_sum += int(num_str)
    
    return total_sum

