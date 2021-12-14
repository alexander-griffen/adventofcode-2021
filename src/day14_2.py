import utils

full_input = utils.get_input()

template = full_input[0]
first = template[0]
last = template[-1]
rules_list = [x.split(' -> ') for x in full_input[2:]]
rules_dict = dict(rules_list)
count_dict_empty = dict(zip([a[0] for a in rules_list], [0 for x in rules_list]))
count_dict = count_dict_empty.copy()
for i, x in enumerate(template):
    if i != len(template) - 1:
        count_dict[x + template[i + 1]] += 1

for i in range(40):
    new_count_dict = count_dict_empty.copy()
    for pair, count in count_dict.items():
        insertion = rules_dict[pair]
        new_count_dict[pair[0]+insertion] += count
        new_count_dict[insertion+pair[1]] += count
    count_dict = new_count_dict.copy()

counts = {}
for pair, count in count_dict.items():
    for letter in pair:
        if letter in counts:
            counts[letter] += count
        else:
            counts[letter] = count

counts[first] += 1
counts[last] += 1
counts = {key:val/2 for key, val in counts.items()}

counts = list(counts.values())

print(max(counts) - min(counts))