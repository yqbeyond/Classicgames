
def init_grid(grid, filename):
    fs = open(filename)
    line = fs.readline().split()
    line = [int(line[i]) for i in range(len(line))]
    while line:
        grid.append(line)
        line = fs.readline().split()
        line = [int(line[i]) for i in range(len(line))]
    fs.close()

def print_grid(grid):
    for i in range(len(grid)):
        print grid[i]

def solve(grid, selects):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            i_area = i / 3 * 3
            j_area = j / 3 * 3
            selects[i][j] = set(range(1, len(grid[i]) + 1)).\
                    difference(set(grid[i]).\
                    union(set([grid[k][j] for k in range(len(grid))])).\
                    union(set(grid[i_area][j_area:j_area+3] + grid[i_area+1][j_area:j_area+3]+grid[i_area+2][j_area:j_area+3])).\
                    difference(set([0])))

    dfs(grid, selects)

def dfs(grid, selects0):
    if ok(grid) == True:
        print "\nThe ans is: "
        print_grid(grid)
        exit(0)

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                if len(selects[i][j]) == 0:
                    return False

                for item in selects[i][j]:
                    grid[i][j] = item
                    update(selects, i, j, item)
                    if (check(grid) == True):
                        if dfs(grid, selects) == False:
                            recover(selects, i, j, item)
                            grid[i][j] = 0

                    else: 
                        recover(selects, i, j, item)
                        grid[i][j] = 0

                if grid[i][j] == 0:
                    return False
                        

def check(grid):
    for i in range(9):
        rows= [grid[i][j] for j in range(9) if grid[i][j] != 0]
        if len(set(rows)) != len(rows):
            return False
        cols = [grid[k][i] for k in range(9) if grid[k][i] != 0]
        if len(set(cols)) != len(cols):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            area = [grid[i][k] for k in range(j, j+3) if grid[i][k] != 0]
            area += [grid[i+1][k] for k in range(j, j+3) if grid[i+1][k] != 0]
            area += [grid[i+2][k] for k in range(j, j+3) if grid[i+2][k] != 0]
            if len(set(area)) != len(area):
                return False

    return True


    '''
    for i in range(len(selects)):
        for j in range(len(selects)):
            print selects[i][j]
    '''

def update(selects, i, j, num):
    
    for m in range(9):
        selects[i][m] = selects[i][m].difference(set([num]))
    for m in range(9):
        selects[m][j] = selects[m][j].difference(set([num]))

    i_area = i / 3 * 3
    j_area = j / 3 * 3

    for m in range(i_area, i_area + 3):
        for n in range(j_area, j_area + 3):
            selects[m][n] = selects[m][n].difference(set([num]))

def ok(grid):
    for i in range(9):
        if set(grid[i]) != set(range(1,10)):
            return False
        if set([grid[k][i] for k in range(9)]) != set(range(1, 10)):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            area = grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3]
            if set(area) != set(range(1, 10)):
                return False

    return True


def recover(selects, i, j, num):
    for m in range(9):
        selects[i][m] = selects[i][m].union(set([num]))
    for m in range(9):
        selects[m][j] = selects[m][j].union(set([num]))

    i_area = i / 3 * 3
    j_area = j / 3 * 3

    for m in range(i_area, i_area + 3):
        for n in range(j_area, j_area + 3):
            selects[m][n] = selects[m][n].union(set([num]))
    

if __name__ == "__main__":
    grid = []
    init_grid(grid, 'game.txt')
    print "Source array is: "
    print_grid(grid)
    selects = [[{} for j in range(len(grid[i]))] for i in range(len(grid))]
    solve(grid, selects)

