import utils

initial_string = utils.get_input()
initial = [int(x) for x in initial_string[0].split(',')]

fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for fish in initial:
    fishes[fish] += 1

for i in range(256):
    new_fishes = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for j in range(1, 9):
        new_fishes[j-1] = fishes[j]
    new_fishes[6] += fishes[0]
    new_fishes[8] += fishes[0]
    fishes = new_fishes.copy()

print(sum(fishes))