import utils
from statistics import mode

binary_input = utils.get_input()

binary_input_lists = [list(x) for x in binary_input]

print(binary_input_lists)
gamma_rate_string = ''
for i in range(len(binary_input_lists[0])):
    gamma_rate_string += mode([x[i] for x in binary_input_lists])

gamma_rate= int(gamma_rate_string, 2)
epsilon_rate_string_unflipped = str(bin(gamma_rate))[2:]
epsilon_rate_string = ['1' if x == '0' else '0' for x in epsilon_rate_string_unflipped]
epsilon_rate_string = ''.join(epsilon_rate_string)
epsilon_rate = int(epsilon_rate_string, 2)

print(gamma_rate * epsilon_rate)