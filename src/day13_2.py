import utils

sheet = utils.get_input()

coords = []
folds = []
for x in sheet:
    if x != '':
        if x[0].isalpha():
            c = x.split(' ')[-1].split('=')
            folds.append([c[0], int(c[1])])
        elif x[0].isnumeric():
            coords.append([int(y) for y in x.split(',')])

max_x = 0
max_y = 0
for i in coords:
    if i[0] > max_x:
        max_x = i[0]
    if i[1] > max_y:
        max_y = i[1]

transparent = [[0 for i in range(max_x + 1)] for j in range(max_y + 1)]

# Fill out the page
for dot in coords:
    transparent[dot[1]][dot[0]] = 1

for fold in folds:
    gap = fold[1]
    if fold[0] == 'y':
        #fold UP
        new_transparent = transparent[:gap]
        old_transparent = transparent[gap:]
        for y, row in enumerate(old_transparent):
            for x, point in enumerate(row):
                if point == 1 and y >= 0:
                    new_transparent[gap - y][x] = 1
    else:
        #fold LEFT
        new_transparent = [row[:gap] for row in transparent]
        old_transparent = [row[gap:] for row in transparent]
        for y, row in enumerate(old_transparent):
            for x, point in enumerate(row):
                if point == 1 and x >= 0:
                    new_transparent[y][gap - x] = 1
    transparent = new_transparent

for row in transparent:
    print(''.join(['o ' if i == 1 else '  ' for i in row]))

