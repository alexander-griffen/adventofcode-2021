import utils
inp = utils.get_input()

counter = 0
for i, num in enumerate(inp):
    if i != 0:
        if int(num) > int(inp[i-1]):
            counter += 1

print(counter)
