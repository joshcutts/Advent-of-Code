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

'''
- search range from start to 12 from end for highest digit
- search range from start to 11 from end for highest digit

'''

def find_max_in_range(bank):
    numerical_bank = [int(digit) for digit in bank]

    max_digit = max(numerical_bank)
    max_index = numerical_bank.index(max_digit)

    return [max_digit, max_index]

# print(find_max_in_range('2342'))

def find_12_digit_max_joltage(bank):
    max_joltage = ''
    start = 0

    while len(max_joltage) < 12:
        remaining = 12 - len(max_joltage) - 1
        # print(bank[start:-remaining], start, remaining, max_joltage, bank)
        
        bank_range = bank[start:] if remaining == 0 else bank[start:-remaining]
        digit, index = find_max_in_range(bank_range)
        start += index + 1
        max_joltage += str(digit)
    
    return max_joltage

# print(find_12_digit_max_joltage('987654321111111') == '987654321111')
# print(find_12_digit_max_joltage('123456789012345'))
# print(find_12_digit_max_joltage('811111111111119') == '811111111119')
# print(find_12_digit_max_joltage('234234234234278') == '434234234278')
# print(find_12_digit_max_joltage('818181911112111') == '888911112111')


def calculate_total_max_joltage(banks):
    total_max_joltage = 0

    for bank in banks:
        total_max_joltage += int(find_12_digit_max_joltage(bank))

    return total_max_joltage




# banks = parse_input('example.txt')
banks = parse_input('puzzle.txt')
print(calculate_total_max_joltage(banks))