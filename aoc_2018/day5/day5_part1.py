import math

def parse_input(file):
    with open(file, "r") as f:
        # lines = f.read().splitlines()
        lines = f.read()
    
    return lines

# polymer = "dabAcCaCBAcCcaDA"
polymer = parse_input('test.txt')
# print(type(polymer))

def find_nonreactive(polymer):
    i = 0
    length = len(polymer) - 1

    while i < length:
        curr = polymer[i]
        next = polymer[i + 1]

        if curr != next and curr.lower() == next.lower():
            # print(curr, next)
            polymer = polymer[0:i] + polymer[i+2:]
            length -= 2
            i -= 1
            # print(i, polymer)
        else:
            i += 1
    
    return len(polymer)

alphabet = list("abcdefghijklmnopqrstuvwxyz")

def find_min(polymer):
    min_length = len(polymer)

    for letter in alphabet:
        sub_polymer = polymer.replace(letter, '').replace(letter.upper(), '')
        count = find_nonreactive(sub_polymer)
        min_length = min(count, min_length)

    return min_length


# print(find_nonreactive(polymer))
print(find_min(polymer))