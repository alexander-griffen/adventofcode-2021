import utils
lines_raw = utils.get_input()

lines_separated = [line.split(' -> ') for line in lines_raw]

lines = []
for line in lines_separated:
    new_line = [coord.split(',') for coord in line]
    new_line = [[int(coord[0]), int(coord[1])] for coord in new_line]
    lines.append(new_line)

def is_horizontal(line):
    if line[0][1] == line[1][1]:
        return True
    return False

def is_vertical(line):
    if line[0][0] == line[1][0]:
        return True
    return False

# Get the largest x and y coordinates in the set
largest_x = 0
largest_y = 0
for line in lines:
    for coord in line:
        if coord[0] > largest_x:
            largest_x = coord[0]
        if coord[1] > largest_y:
            largest_y = coord[1]

space = [[0 for x in range(largest_x + 1)] for y in range(largest_y + 1)]

for line in lines:
    if is_horizontal(line):
        y = line[0][1]
        start = min(line[0][0], line[1][0])
        end = max(line[0][0], line[1][0])

        for x in range(start, end+1):
            space[y][x] += 1

    if is_vertical(line):
        x = line[0][0]
        start = min(line[0][1], line[1][1])
        end = max(line[0][1], line[1][1])
        for y in range(start, end+1):
            space[y][x] += 1



count = 0
for row in space:
    print(row)
    for i in row:
        if i >= 2:
            count += 1

print(count)