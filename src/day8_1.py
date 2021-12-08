import utils

notes = utils.get_input()
outputs = [note.split(' | ')[1] for note in notes]
outputs = [output.split() for output in outputs]

nums = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

unique = [2, 4, 3, 7]
counts = 0
for output in outputs:
    for num in output:
        if len(num) in unique:
            counts += 1

print(counts)