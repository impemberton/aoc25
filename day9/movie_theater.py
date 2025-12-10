coords = []
with open("input.txt") as input:
    for line in input:
        x, y = line.split(",")
        coords.append((int(x),int(y)))

areas = []
for i, (x1, y1) in enumerate(coords):
    for x2, y2 in coords[i+1:]:
        area = (abs(x1-x2)+1) * (abs(y1-y2)+1)
        areas.append(area)

print(max(areas))

