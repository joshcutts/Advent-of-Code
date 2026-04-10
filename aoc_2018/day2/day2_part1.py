from collections import Counter

def parse_input(filename):
    with open(filename, "r") as f:
        lines = f.read().splitlines()

    return lines

def calculate_checksum(ids):
    two_count = 0
    three_count = 0

    for id in ids:
        id_count = Counter(id)
        counts = id_count.values()
        if 2 in counts:
            two_count += 1
        
        if 3 in counts:
            three_count += 1
    
    return two_count * three_count

# print(parse_input('example.txt'))
# ids = parse_input('example.txt')
ids = parse_input('puzzle.txt')
print(calculate_checksum(ids))