def solution(a, b, c, d):
    
    result = 0
    dice = [a,b,c,d]
    
    if len(set(dice)) == 1 :
        result = 1111 * max(dice)
    
    if len(set(dice)) == 4 : 
        result = min(dice)
        
    if len(set(dice)) == 2 :
        if dice.count(max(dice)) == 3 :
            p = max(dice)
            q = min(dice)
            result = (10*p+q)**2
        if dice.count(min(dice)) == 3:
            p = min(dice)
            q = max(dice)
            result = (10*p+q)**2
        if dice.count(max(dice)) == 2 :
            p = min(dice)
            q = max(dice)
            result = (p + q) * abs(p - q)
            
    if len(set(dice)) == 3 :
        sorted_dice = sorted(dice)
        if sorted_dice[0] == sorted_dice[1] :
            p = sorted_dice[0]
            q = sorted_dice[2]
            r = sorted_dice[3]
            result = q * r
        if sorted_dice[1] == sorted_dice[2] : 
            p = sorted_dice[1]
            q = sorted_dice[3]
            r = sorted_dice[0]
            result = q * r                
        if sorted_dice[2] == sorted_dice[3] : 
            p = sorted_dice[2]
            q = sorted_dice[1]
            r = sorted_dice[0]
            result = q * r                  
    return result

