import utils

full_input = utils.get_input()

template = full_input[0]

rules_list = [x.split(' -> ') for x in full_input[2:]]
rules_dict = dict(rules_list)
for i in range(10):
    new_insertions = []
    for i, x in enumerate(template):
        if i != len(template) - 1:
            new_insertions.append(rules_dict[x+template[i+1]])

    new_template = []
    for i in range(len(template)):
        new_template.append(template[i])
        if i != len(template) - 1:
            new_template.append(new_insertions[i])
    template = new_template

counts = {}
for letter in template:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1

highest = 0
lowest = None
for key, value in counts.items():
    if value > highest:
        highest = value
    if not lowest:
        lowest = value
    elif value < lowest:
        lowest = value

print(highest-lowest)