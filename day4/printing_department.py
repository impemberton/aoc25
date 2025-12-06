with open("input.txt") as input:
    grid = [line.strip() for line in input]

accessible = 0

for r in range(0, len(grid)):
    for c in range(0, len(grid[0])):
        if grid[r][c] == "@":
            print(f"Roll found at row: {r}, col: {c}")
            adjacent = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    print(f"checking for adjacent roll at row: {r+i}, col: {c+j}")
                    if r+i >= 0 and r+i < len(grid):
                        if c+j >= 0 and c+j < len(grid[0]):
                            if grid[r+i][c+j] == "@" and not (i == 0 and j == 0):
                                adjacent += 1
            if adjacent < 4:
                accessible += 1

print("Number of rolls accessible: ", accessible)
            
