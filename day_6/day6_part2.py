import math
import re

def parse_input(filename):
    with open(filename, 'r') as f:
        raw_input = [line for line in f.read().splitlines()]

    return raw_input

def vertical_align_problems(raw_input):
    problems = []
    operators = raw_input[-1].split()
    problem = []
    skip = False
    for col in range(len(raw_input[0])):
        if skip:
            print(problem)
            problems.append(problem)
            problem = []
            skip = False
            next
        num = ''
        for row in range(len(raw_input[0:-1])):
            num += raw_input[row][col]
        if all(x == ' ' for x in num.split()):
            skip = True
        else:
            problem.append(num)
            num = ''

    problems.append(problem)

    combined_data = list(zip(problems, operators))
    return [numbers + [operator] for numbers, operator in combined_data]

def calculate_total(problems):
    total = 0

    for problem in problems:
        operator = problem.pop()
        int_problem = [int(num) for num in problem]

        if operator == '+':
            total += sum(int_problem)
        else:
            total += math.prod(int_problem)

    return total

# raw_input = parse_input('example.txt')
raw_input = parse_input('puzzle.txt')
problems = vertical_align_problems(raw_input)
# print(problems)
print(calculate_total(problems))
