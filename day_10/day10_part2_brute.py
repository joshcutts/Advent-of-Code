"""

[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}


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
from datetime import datetime



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


def find_min_button_presses(light_diagram, buttons):
    combinations = max(light_diagram)
    length = len(light_diagram)
    


    while True:
        combos = [list(c) for c in combinations_with_replacement(buttons, combinations)]

        for combo in combos:
            first_button = combo[0]
            # print(all(button == first_button for button in combo))
            if all(button == first_button for button in combo):
                continue

            test_state = generate_joltage(combo, length)
            if test_state == light_diagram:
                return combinations

        combinations += 1
        if (combinations == 1000):
            break


def sum_total_button_presses(machines):
    total_button_presses = 0
    machine_count = len(machines)
    for i, machine in enumerate(machines):
        now = datetime.now()
        print(now.strftime("%Y-%m-%d %H:%M:%S"))
        print("calculating machine: ", i, "/", machine_count)
        joltages, buttons = machine
        total_button_presses += find_min_button_presses(joltages, buttons)

    return total_button_presses

# raw_machines = parse_input('example.txt')
raw_machines = parse_input('puzzle.txt')
formatted_machines = format_input(raw_machines)
# print(formatted_machines)
print(sum_total_button_presses(formatted_machines))
