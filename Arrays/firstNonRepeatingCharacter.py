def firstNotRepeatingCharacter(s):
    
    chars = {}
    
    index = 0
    for i in s:
        if i in chars:
            chars[i].append(index)
        else:
            chars[i] = [index]
        index += 1

    leastIndex = -1
    for c in chars:
        if len(chars[c]) == 1:
            if leastIndex == -1 or chars[c][0] < leastIndex:
                leastIndex = chars[c][0]
                
    if leastIndex < 0:
        return '_'
    else:
        return s[leastIndex]
    