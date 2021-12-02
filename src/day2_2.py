import utils

inp = utils.get_input()

x = 0
y = 0
aim = 0

for movement in inp:
    direction, magnitude = movement.split()
    magnitude = int(magnitude)
    if direction == 'forward':
        x += magnitude
        y+= magnitude*aim
    elif direction == 'up':
        aim -= magnitude
    elif direction == 'down':
        aim += magnitude

print(x*y)