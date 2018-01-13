def isCryptSolution(crypt, solution):
    solutionDict = {}
    for s in solution:
        solutionDict[str(s[0])] = str(s[1])
    
    cryptMapped = []
    for word in crypt:
        cMap = ""
        for letter in word:
            cMap += solutionDict[letter]
        cryptMapped.append(cMap)

    if len(str(int(cryptMapped[0]))) != len(str(cryptMapped[0])):
        return False
    if len(str(int(cryptMapped[1]))) != len(str(cryptMapped[1])):
        return False
    if len(str(int(cryptMapped[2]))) != len(str(cryptMapped[2])):
        return False
    if int(cryptMapped[0]) + int(cryptMapped[1]) == int(cryptMapped[2]):
        return True

    return False
