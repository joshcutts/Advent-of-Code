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

def format_input(lines):
    formatted_input = []

    for line in lines:
        arr = line.split(' ')
        light_diagram = format_light_diagram(arr[0])
        buttons = format_buttons(arr[1:-1])
        formatted_input.append([light_diagram, buttons])

    return formatted_input

def generate_diagram(buttons, length):
    diagram = [0] * length

    for button in buttons:
        for b in button:
            if diagram[b] == 0:
                diagram[b] = 1
            else:
                diagram[b] = 0
    
    return diagram

print(generate_diagram([[3], [1, 3], [2]], 4)) # [0, 1, 1, 0]

def find_min_button_presses(light_diagram, buttons):
    combinations = 1
    length = len(light_diagram)

    while True:
        combos = [list(c) for c in combinations_with_replacement(buttons, combinations)]

        for combo in combos:
            
            test_state = generate_diagram(combo, length)
            if test_state == light_diagram:
                return combinations

        combinations += 1
        if (combinations == 10):
            break


# print(find_min_button_presses([0, 1, 1, 0], [[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]])) # 2


def sum_total_button_presses(machines):
    total_button_presses = 0

    for machine in machines:
        light_diagram, buttons = machine
        total_button_presses += find_min_button_presses(light_diagram, buttons)

    return total_button_presses

# lines = parse_input('example.txt')
raw_machines = parse_input('puzzle.txt')
formatted_machines = format_input(raw_machines)
print(sum_total_button_presses(formatted_machines))
