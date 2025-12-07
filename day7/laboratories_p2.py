input = open("input.txt")
grid = [list(line.strip()) for line in input]
splits = 0
rows_left = len(grid)
while rows_left > 1:
    for c in range(len(grid[0])):
        if grid[0][c] == "S":
            grid[1][c] = 1
        if  isinstance(grid[0][c], int):
            if grid[1][c] == "^":
                if grid[1][c-1] == ".":
                    grid[1][c-1] = grid[0][c]
                else:
                    grid[1][c-1] += grid[0][c]
                
                if grid[1][c+1] == ".":
                    grid[1][c+1] = grid[0][c]
                else:
                    grid[1][c+1] += grid[0][c]
                splits += 1
            else:
                if grid[1][c] == ".":
                    grid[1][c] = grid[0][c]
                else:
                    grid[1][c] += grid[0][c]
    del grid[0]
    rows_left -= 1
possibilities = 0
for item in grid[0]:
    if isinstance(item, int):
        possibilities += item

print(splits) 
print(possibilities)
