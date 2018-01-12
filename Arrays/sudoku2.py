def sudoku2(grid):
    # Check rows
    for row in grid:
        vals = {}
        for val in row:
            if val in vals and val != '.':
                return False
            vals[val] = True

    # Check columns
    for i in range(len(grid)):
        column = [row[i] for row in grid]
        vals = {}
        for val in column:
            if val in vals and val != '.':
                return False
            vals[val] = True
    
    # Check blocks
    for rowTuple in [(0, 3), (3, 6), (6, 9)]:
        for colTuple in [(0, 3), (3, 6), (6, 9)]:
            vals = {}
            for i in range(rowTuple[0], rowTuple[1]):
                for j in range(colTuple[0], colTuple[1]):
                    val = grid[i][j]
                    if val in vals and val != '.':
                        return False
                    vals[val] = True

    return True
