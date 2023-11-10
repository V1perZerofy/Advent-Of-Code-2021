def openFile():
    with open("Day 3/Input/input.txt") as f:
        #2d array
        grid = [[i for i in line.strip()] for line in f.readlines()]
        print(len(grid))
        width = len(grid[0])
        #close file
        f.close()
    return grid, width

def part2(grid, width):
    for j in range(width):
        height = len(grid)
        x = 0
        y = 0
        more = 0
        temp = []
        for i in range(height):
            if grid[i][j] == '0':
                x += 1
            elif grid[i][j] == '1':
                y += 1
        #print(x, y)
        if x > y:
            more = 0
        elif y > x:
            more = 1
        for i in range(height):
            if grid[i][0] == str(more):
                temp.append(grid[i])
        #print(len(temp))
        #overwriting grid
        grid = temp
        print(len(grid))
        #print(grid)

part2(openFile())
