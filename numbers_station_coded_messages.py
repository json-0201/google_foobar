def solution(l, t):
    
    for i in range(len(l)):
        total = 0
        
        for j in range(i, len(l)):
            total += l[j]
            
            if total == t:
                return [i,j]
    return [-1,-1]


solution([2,4,5,7], 11)