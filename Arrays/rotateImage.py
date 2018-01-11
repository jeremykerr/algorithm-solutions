
def rotateImage(a):
    r = [x[:] for x in a]

    l = len(a)
    for i in range(l):
        for j in range(l):
            r[j][l-1-i] = a[i][j]
    
    return r