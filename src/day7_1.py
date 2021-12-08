import utils

initial_string = utils.get_input()
initial = [int(x) for x in initial_string[0].split(',')]
min_fuel = None
for i in range(min(initial), max(initial)+1):
    differences = [abs(x-i) for x in initial]
    if not min_fuel:
        min_fuel = sum(differences)
    if sum(differences) < min_fuel:
        min_fuel = sum(differences)

print(min_fuel)