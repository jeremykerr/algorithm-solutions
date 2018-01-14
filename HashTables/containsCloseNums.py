def containsCloseNums(nums, k):
    numDict = {}
    for index in range(len(nums)):
        val = nums[index]
        if val not in numDict:
            numDict[val] = []
        numDict[val].append(index)
    
    for num in sorted(numDict):
        prev = None
        for index in numDict[num]:
            if prev is None:
                pass
            elif index - prev <= k:
                return True
            prev = index
    
    return False
