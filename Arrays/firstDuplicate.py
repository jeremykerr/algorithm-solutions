def firstDuplicate(a):
    
    seen = {}
    
    for i in a:
        if i in seen:
            return i
        seen[i] = True
    
    return -1
