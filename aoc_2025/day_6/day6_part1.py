import math

def parse_input(filename):
    with open(filename, 'r') as f:
        raw_input = [line.split() for line in f.read().splitlines()]

    for i, line in enumerate(raw_input[:-1]):
        raw_input[i] = [int(n) for n in line]

    return raw_input

def vertical_align_problems(raw_input):
    problems = []

    for row in range(len(raw_input[0])):
        problem = []
        for col in range(len(raw_input)):
            problem.append(raw_input[col][row])

        problems.append(problem)
    
    return problems

def calculate_total(problems):
    total = 0

    for problem in problems:
        operator = problem.pop()

        if operator == '+':
            total += sum(problem)
        else:
            total += math.prod(problem)

    return total



# raw_input = parse_input('example.txt')
raw_input = parse_input('puzzle.txt')
problems = vertical_align_problems(raw_input)
print(calculate_total(problems))



