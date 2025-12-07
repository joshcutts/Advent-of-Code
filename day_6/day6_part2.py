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

def transform_problem(original, operator):
    max_length = (max([len(str(n)) for n in original]))
    
    if operator == '+':
        justified = [str(n).ljust(max_length, ' ') for n in original]
    else:
        justified = [str(n).rjust(max_length, ' ') for n in original]
    
    matrix_digits = [list(n) for n in justified]

    transformed = []

    for col in range(len(matrix_digits[0]) - 1, -1, -1):
        new_num = ''
        for row in range(0, len(matrix_digits)):
            new_num += matrix_digits[row][col]
        
        transformed.append(new_num)

    return [int(x) for x in transformed]

def calculate_total(problems):
    total = 0

    for problem in problems:
        operator = problem.pop()
        transformed_problem = transform_problem(problem, operator)
        print(transformed_problem)
        if operator == '+':
            total += sum(transformed_problem)
        else:
            total += math.prod(transformed_problem)

    return total

# def write_to_txt(arr, filename):
#     separator = ' '
#     with open(filename, 'w') as f:
#         for subarray in arr:
#             # 1. Join the elements of the subarray into a single string
#             line = separator.join([str(n) for n in subarray])
            
#             # 2. Write the string to the file, followed by a newline character (\n)
#             f.write(line + '\n')

raw_input = parse_input('example.txt')
# raw_input = parse_input('puzzle.txt')
# print(raw_input)
# write_to_txt([raw_input], 'raw_input_format.txt')
# print(len(raw_input), len(raw_input[0]), len(raw_input[1]))
problems = vertical_align_problems(raw_input)
# write_to_txt(problems, 'vertical_problems.txt')
# write_to_txt([transform_problem(problem, problem.pop()) for problem in problems], 'final_transformed.txt')
# print(problems)
print(calculate_total(problems))
# print(transform_problem([64, 23, 314], '+'))
# print(transform_problem([51, 387, 215], '*'))


