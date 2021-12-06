import utils

initial_string = utils.get_input()
initial = [int(x) for x in initial_string[0].split(',')]

fishes = initial.copy()
for i in range(80):
    new_fishes = []
    for fish in fishes:
        if fish == 0:
            new_fishes.append(6)
            new_fishes.append(8)
        else:
            new_fishes.append(fish-1)
    fishes = new_fishes.copy()

print(len(fishes))

