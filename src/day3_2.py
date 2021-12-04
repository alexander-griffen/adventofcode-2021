import utils
from statistics import multimode

binary_input = utils.get_input()

binary_input_lists = [list(x) for x in binary_input]

length = len(binary_input_lists[0])

# Find the oxygen generator rating

o2_possible_answers = binary_input_lists.copy()
for i in range(length):
    most_common_bit_list = multimode([x[i] for x in o2_possible_answers])
    if len(most_common_bit_list) == 2 or most_common_bit_list[0] == '1':
        most_common_bit = '1'
    else:
        most_common_bit = '0'
    new_possible_answers = []
    for j in o2_possible_answers:
        if j[i] == most_common_bit:
            new_possible_answers.append(j)
    o2_possible_answers = new_possible_answers
    if len(o2_possible_answers) == 1:
        break


# Find CO2 rating
co2_possible_answers = binary_input_lists.copy()
for i in range(length):
    most_common_bit_list = multimode([x[i] for x in co2_possible_answers])
    if len(most_common_bit_list) == 2 or most_common_bit_list[0] == '1':
        least_common_bit = '0'
    else:
        least_common_bit = '1'
    new_possible_answers = []
    for j in co2_possible_answers:
        if j[i] == least_common_bit:
            new_possible_answers.append(j)
    co2_possible_answers = new_possible_answers
    if len(co2_possible_answers) == 1:
        break


o2_answer = ''.join(o2_possible_answers[0])
co2_answer = ''.join(co2_possible_answers[0])
print(int(o2_answer, 2) * int(co2_answer, 2))


