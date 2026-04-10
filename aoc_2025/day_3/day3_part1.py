import math
"""


Linear search with two pointers for top 2 highest numbers
  a          r
234234234234278
"""
negative_inifity = -math.inf

def parse_input(filename):
    with open(filename, "r") as f:
        banks = f.read().splitlines()

    return banks

def find_max_joltage(bank):
    a = 0
    r = 1
    final_first_digit = bank[0]
    final_second_digit = bank[1]

    while r < len(bank):
        first_digit = bank[a]
        second_digit = bank[r]

        if int(second_digit) > int(first_digit) and r != len(bank) - 1:
            a = r
            r = a
            final_first_digit = bank[a]
            final_second_digit = bank[r + 1]
            
        elif int(second_digit) > int(final_second_digit):
            final_second_digit = bank[r]
        
        r += 1
    
    return int(final_first_digit + final_second_digit)

def calculate_total_max_joltage(banks):
    total_max_joltage = 0

    for bank in banks:
        total_max_joltage += find_max_joltage(bank)

    return total_max_joltage


# print(find_max_joltage("987654321111111"))
# print(find_max_joltage("811111111111119"))
# print(find_max_joltage("234234234234278"))
# print(find_max_joltage("818181911112111"))


# banks = parse_input('example.txt')
banks = parse_input('puzzle.txt')
print(calculate_total_max_joltage(banks))