import utils

notes = utils.get_input()

nums = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

unique = {2: 1, 4: 4, 3: 7, 7: 8}
output_values = []
for note in notes:
    mapping = {}
    letter_mapping = {}
    inp = note.split(' | ')[0].split()
    out = note.split(' | ')[1].split()

    inp = ["".join(sorted(x)) for x in inp]
    out = ["".join(sorted(x)) for x in out]

    for i in inp:
        if len(i) in unique:
            mapping[unique[len(i)]] = i

    #get counts for every (fake) letter
    letter_counts = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    for number in inp:
        for letter in number:
            letter_counts[letter] += 1

    d_and_g = []
    a_and_c = []
    for key, value in letter_counts.items():
        if value == 6:
            letter_mapping['b'] = key
        elif value == 8:
            a_and_c.append(key)
        elif value == 4:
            letter_mapping['e'] = key
        elif value == 9:
            letter_mapping['f'] = key
        elif value == 7:
            d_and_g.append(key)
    if d_and_g[0] in mapping[4]:
        letter_mapping['d'] = d_and_g[0]
        letter_mapping['g'] = d_and_g[1]
    else:
        letter_mapping['d'] = d_and_g[1]
        letter_mapping['g'] = d_and_g[0]

    if a_and_c[0] in mapping[1]:
        letter_mapping['c'] = a_and_c[0]
        letter_mapping['a'] = a_and_c[1]
    else:
        letter_mapping['c'] = a_and_c[1]
        letter_mapping['a'] = a_and_c[0]

    #Now we have a full letter mapping, make a dictionary
    for i in range(10):
        mapping[i] = "".join(sorted([letter_mapping[letter] for letter in nums[i]]))

    # Turn mapping dictionary inside out
    mapping = dict(zip(mapping.values(), mapping.keys()))
    output_num = ""
    for o in out:
        output_num += str(mapping["".join(sorted(o))])
    output_values.append(int(output_num))

print(sum(output_values))

