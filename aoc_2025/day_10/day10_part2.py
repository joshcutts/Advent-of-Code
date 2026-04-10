"""

[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}

[7,5,12,7,2]

[[0,2,3,4], [2,3], [0,4], [0,1,2], [1,2,3,4]]
0  1  2  3  4 - index
7  5  12 7  2 - joltage

0  0  0  0  0  - (0, 2, 3, 4) (1) - select longest length button

1  0  1  1  1  - current sum (2)
6  5  11 6  1  - difference. highest 2, 0, 3, 4 -> (0,2,3,4)

2  0  2  2  2  - current sum (3)
5  5  10 5  0  - difference. highest 2, 0, 1, 3. exclude 4 -> (0, 1, 2)

3  1  3  2  2  - current sum (4)
4  4  9  5  0  - difference. highest 2, 3, 0, 1. exclude 4 -> (2, 3)

3  1  4  3  2  - current sum (5)
4  4  8  4  0  - difference. highest 2, 0, 1, 3.  exclude 4 -> (0, 1, 2)

4  2  5  3  2  - current sum (6)
3  3  7  4  0  - difference. highest 2, 3, 0, 1.  exclude 4 -> (2, 3)

4  2  6  4  2  - current sum (7)
3  3  6  3  0  - difference. highest 2, 0, 1, 3.  exclude 4 -> (0, 1, 2)

5  3  7  4  2  - current sum (8)
2  2  5  3  0 - difference. highest 2, 3, 0, 1.  exclude 4 -> (2, 3)

5  3  8  5  2  - current sum (9)
2  2  4  2  0 - difference. highest 2, 0, 1, 3.  exclude 4 -> (0, 1, 2)

6  4  9  5  2  - current sum (10)
1  1  3  2  0 - difference. highest 2, 3, 0, 1.  exclude 4 -> (2, 3)

6  4  10  6  2  - current sum (11)
1  1  2   1  0 - difference. highest 2, 0, 1, 3.  exclude 4 -> (0, 1, 2)

7  5  11  6  2  - current sum (12)
0  0  1   1  0 - difference. highest 2, 3.  exclude 0, 1, 4 -> (2, 3)

7  5  12  7  2  - current sum (final)
0  0  0   0  0 - difference.

"""

from itertools import combinations_with_replacement

def parse_input(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    return lines

def format_light_diagram(string_light_diagram):
    s = string_light_diagram[1:-1]

    return [0 if char == '.' else 1 for char in s]

def format_buttons(string_buttons):
    remove_parans = [s.replace('(', '').replace(')', '') for s in string_buttons]
    return [list(map(int, button.split(','))) for button in remove_parans]

def format_joltages(string_joltages):
    remove_brackets = string_joltages.replace('{', '').replace('}', '')
    return [int(j) for j in remove_brackets.split(',')]

def format_input(lines):
    formatted_input = []

    for line in lines:
        arr = line.split(' ')
        # light_diagram = format_light_diagram(arr[0])
        buttons = format_buttons(arr[1:-1])
        joltages = format_joltages(arr[-1])
        formatted_input.append([joltages, buttons])

    return formatted_input

def generate_joltage(buttons, length):
    diagram = [0] * length

    for button in buttons:
        for b in button:
            diagram[b] += 1
    
    return diagram

def rank_indices_by_difference(difference_joltage):
    difference_joltage_w_index = [[i, jolt] for i, jolt in enumerate(difference_joltage)]
    # print('diff',difference_joltage_w_index)
    ranked_indices = []
    for i, j in sorted(difference_joltage_w_index, key=lambda x:(x[1]), reverse=True):
        if j != 0:
            ranked_indices.append(i)

    return ranked_indices

# print(rank_indices_by_difference([6, 5, 11, 6, 1])) # [2, 0, 3, 1, 4]

def find_best_button(difference_joltage, buttons):
    # remove indices that have already reached required joltage (difference_joltage is 0)
    exclude_indices = [i for i, j in enumerate(difference_joltage) if j == 0]
    ranked_indices = rank_indices_by_difference(difference_joltage)
    
    max_score = 0
    selected_button = None
    # print('rank', ranked_indices)
    for button in buttons:
        length = len(button)
        score = 0
        # print(button)
        for position in button:
            if position in exclude_indices:
                score -= 1000
            if position in ranked_indices:
                multiplier = length - (ranked_indices.index(position))
                score += multiplier
        # print(button, score, max_score)
        if score > max_score:
            # print(button, max_score)
            max_score = score
            selected_button = button

    return selected_button


# print(find_best_button([5,5,10,5,0], [[0,2,3,4], [2,3], [0,4], [0,1,2], [1,2,3,4]]))
# print(find_best_button([3, 3, 3, 4], [[1,3], [2], [2,3], [0,2], [0,1]]))


def find_max_length_button(buttons):
    max_length_button = []

    for button in buttons:
        if len(button) > len(max_length_button):
            max_length_button = button

    return max_length_button

# print(find_max_length_button([[0,2,3,4], [2,3], [0,4], [0,1,2], [1,2,3,4]]))

def subtract_button(difference, button):
    # print('subtract', button)
    for b in button:
        # print(b, difference[b])
        difference[b] -= 1
    
    return difference

# print(subtract_button([7, 5, 12, 7, 2], [0, 2, 3, 4])) # [6, 5, 11, 6, 1]

def find_minimum_joltage_button_presses(final_joltage, buttons):
    max_length_button = find_max_length_button(buttons)
    # print('max length button', max_length_button)
    difference = final_joltage.copy()
    difference = subtract_button(difference, max_length_button)
    # print('first', difference)
    button_count = 1

    while not all(jolt == 0 for jolt in difference):
        # print('prev difference', difference)
        next_button = find_best_button(difference, buttons)
        # print('button', next_button)
        difference = subtract_button(difference, next_button)
        # print('next difference', difference)
        button_count += 1
        

    return button_count

# print(find_minimum_joltage_button_presses([7,5,12,7,2], [[0,2,3,4], [2,3], [0,4], [0,1,2], [1,2,3,4]]))

def sum_total_button_presses(machines):
    total_button_presses = 0

    for machine in machines:
        joltages, buttons = machine
        total_button_presses += find_minimum_joltage_button_presses(joltages, buttons)

    return total_button_presses

def most_constrained(difference, buttons):
    # index that appears in buttons least frequently
    counts = {}
    for button in buttons:
        
        for b in button:
            if b in counts:
                counts[b] += 1
            else:
                counts[b] = 1

    min_count = min(counts.values())
    min_indices = [k for k,v in counts.items() if v == min_count]
    return min_indices

print(most_constrained([52,67,66,109,49,65,70,66,33,72], [(3,6), (0,1,2,3,4,5,7,9), (0,1,5,6,7,8,9), (1,9), (0,1,3,4,5,6,7), (0,1,2,3,4,5), (1,2,3,4,5,6,7,8), (2,3,5,7,8), (2,3,5,7,9), (0,1,2,3,4,6,9), (4,5,6,7,8), (3,6,7,8,9)]))

raw_machines = parse_input('example.txt')
# raw_machines = parse_input('puzzle.txt')
formatted_machines = format_input(raw_machines)
# print(formatted_machines)

print(sum_total_button_presses(formatted_machines))