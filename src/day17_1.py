import utils
info = utils.get_input()

info = info[0][13:]
info = [[int(y) for y in x[2:].split('..')] for x in info.split(', ')]

x_coords = info[0]
y_coords = info[1]

beyond_x = max(x_coords) + 1
beyond_y = min(y_coords) - 1

# generate a list of the target area
target_area = []
for x in range(x_coords[0], x_coords[1]+1):
    for y in range(y_coords[0], y_coords[1]+1):
        target_area.append((x, y))

answers = []
last_y = None
start_x_vel = 1
start_y_vel = 1
for start_x_vel in range(0, 100):
    for start_y_vel in range(0, 100):
        x_pos = 0
        y_pos = 0
        x_vel = start_x_vel
        y_vel = start_y_vel
        highest_y = 0
        while True: # Check these starting velocities
            if y_pos > highest_y:
                highest_y = y_pos
            x_pos += x_vel
            y_pos += y_vel
            if x_vel < 0:
                x_vel += 1
            elif x_vel > 0:
                x_vel -= 1
            y_vel -= 1
            if (x_pos, y_pos) in target_area:
                answers.append(highest_y)
                break
            if x_pos >= beyond_x or y_pos <= beyond_y:
                break

print(max(answers))
