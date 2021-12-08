import utils

initial_string = utils.get_input()
initial = [int(x) for x in initial_string[0].split(',')]

differences_list = []
for i in range(min(initial), max(initial)+1):
    differences_list.append([abs(x-i) for x in initial])

max_difference = 0
for differences in differences_list:
    if max(differences) > max_difference:
        max_difference = max(differences)

triangle_numbers_list = []
for i, j in enumerate(range(max_difference + 1)):
    if j == 0:
        triangle_numbers_list.append(0)
    else:
        triangle_numbers_list.append(j + triangle_numbers_list[i-1])

min_fuel = None
for differences in differences_list:
    triangular_differences = [triangle_numbers_list[d] for d in differences]
    if not min_fuel:
        min_fuel = sum(triangular_differences)
    elif sum(triangular_differences) < min_fuel:
        min_fuel = sum(triangular_differences)

print(min_fuel)