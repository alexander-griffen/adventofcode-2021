import utils

lava_input = utils.get_input()

lava_map = []
for row in lava_input:
    lava_map.append([int(x) for x in row])

def check_lowest(x, adj):
    for n in adj:
        if x >= n:
            return False
    return True

low_points = []
for y, row in enumerate(lava_map):
    for x, num in enumerate(row):
        adj = []
        if y != 0:
            adj.append(lava_map[y-1][x])
        if y != len(lava_map)-1:
            adj.append(lava_map[y+1][x])
        if x != 0:
            adj.append(row[x-1])
        if x != len(row)-1:
            adj.append(row[x+1])
        if check_lowest(num, adj):
            low_points.append(num)

print(sum(low_points) + len(low_points))