input = open("input.txt")
grid = [list(line.strip()) for line in input]
splits = 0
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if r > 0 and grid[r-1][c] in "|S":
            if grid[r][c] == "^":
                grid[r][c-1] = "|"
                grid[r][c+1] = "|"
                splits += 1
            else:
                grid[r][c] = "|"

[print("".join(line)) for line in grid]
print(splits) 
