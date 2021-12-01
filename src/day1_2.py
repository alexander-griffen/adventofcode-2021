import utils
inp = utils.get_input()

#get windows
windows = []
for i in range(len(inp)):
    if i + 3 <= len(inp):
        windows.append(sum([int(inp[i]), int(inp[i+1]), int(inp[i+2])]))

#print(windows)

counter = 0
for i, num in enumerate(windows):
    if i != 0:
        if int(num) > int(windows[i-1]):
            counter += 1

print(counter)
