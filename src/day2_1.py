import utils

inp = utils.get_input()

x = 0
y = 0

for movement in inp:
    direction, magnitude = movement.split()
    magnitude = int(magnitude)
    if direction == 'forward':
        x += magnitude
    elif direction == 'up':
        y -= magnitude
    elif direction == 'down':
        y += magnitude

print(x*y)

