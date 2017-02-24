def avg(list = []):

    n = len(list)
    
    for item in range (n-1):
        
        if list[item] > list[item+1]:
            
            max = list[item]
            
            item+=1
            
            continue

    return max

print(avg([8,4,10]))