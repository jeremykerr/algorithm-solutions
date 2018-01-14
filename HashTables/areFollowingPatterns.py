def areFollowingPatterns(strings, patterns):
    patternsDict = {}
    resultsDict = {}
    for index in range(len(strings)):
        key = strings[index]
        val = patterns[index]
        if key in patternsDict:
            if patternsDict[key] != val:
                return False
        if val in resultsDict:
            if resultsDict[val] != key:
                return False
        patternsDict[key] = val
        resultsDict[val] = key

    return True