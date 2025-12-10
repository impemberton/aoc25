original_coords = []
x_values = set()
y_values = set()
with open("input.txt") as input:
    for line in input:
        x, y = line.split(",")
        x_values.add(int(x))
        y_values.add(int(y))
        original_coords.append((int(x),int(y)))
x_values = list(sorted(x_values))
y_values = list(sorted(y_values))


coords = []
for x, y in original_coords:
    coords.append((x_values.index(x), y_values.index(y)))

grid = [["." for i in range(len(x_values))] for j in range(len(y_values))]

for i, (x1, y1) in enumerate(coords):
    grid[y1][x1] = "#"
    
    x2, y2 = coords[i+1] if i < len(coords)-1 else coords[0]

    if x1 == x2:
        r = range(y1+1, y2) if y2 > y1 else range(y2+1, y1)
        for y in r:
            grid[y][x1] = "X"
    else:
        r = range(x1+1, x2) if x2 > x1 else range(x2+1, x1)
        for x in r:
            grid[y1][x] = "X"

for r in range(len(grid)):
    if "X" in grid[r] or "#" in grid[r]:
        first_tile_pos = 0
        last_tile_pos = -1
        while grid[r][first_tile_pos] not in "#X":
            first_tile_pos += 1
        while grid[r][last_tile_pos] not in "#X":
            last_tile_pos -= 1
        last_tile_pos += len(grid[r])
        
        for c in range(first_tile_pos, last_tile_pos):
            if grid[r][c] == ".":
                grid[r][c] = "X"
        


areas = []
for i, (x1, y1) in enumerate(coords):
    for x2, y2 in coords[i+1:]:
        y_range = range(y1, y2+1) if y2 > y1 else range(y2, y1+1)
        x_range = range(x1, x2+1) if x2 > x1 else range(x2, x1+1)
        valid = True
        for r in y_range:
            for c in x_range:
                if grid[r][c] == ".":
                    valid = False
        if valid:
            area = (abs(x_values[x1]-x_values[x2])+1) * (abs(y_values[y1]-y_values[y2])+1)
            areas.append(area)

print(max(areas))
