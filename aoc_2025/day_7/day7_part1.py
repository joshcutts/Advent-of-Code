"""
Docstring for aoc_2025.day_7.day7_part1


.......S.......
.......|.......1
......|^|......2
......|.|......2
.....|^|^|.....3, 5
.....|.|.|.....3, 5
....|^|^|^|....4, 9
....|.|.|.|....4, 9
...|^|^|||^|...6, 11
...|.|.|||.|...6, 11
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.9
|^|^|^|^|^|||^|
|.|.|.|.|.|||.|


"""

def parse_input(filename):
    with open(filename, "r") as f:
        manifold_diagram = [list(line) for line in f.read().splitlines()]
        # manifold_diagram = f.read().splitlines()

    return manifold_diagram

def find_s(manifold):
    for i, char in enumerate(manifold[0]):
        if char == "S":
            return i

def count_splits(manifold, start):
    splits = 0
    manifold[1][start] = '|'
    for row_i, row in enumerate(manifold):
        if row_i == '0':
            next
        for space_i, space in enumerate(row):
            if manifold[row_i - 1][space_i] == '|' and space == '^':
                manifold[row_i + 1][space_i - 1] = '|'
                manifold[row_i + 1][space_i + 1] = '|'
                splits += 1
            elif manifold[row_i - 1][space_i] == '|':
                manifold[row_i][space_i] = '|'
    
    return splits



manifold = parse_input('example.txt')
# manifold = parse_input('puzzle.txt')
start = find_s(manifold)
# print(find_s(manifold))
print(count_splits(manifold, start))
for m in manifold:
    print("".join(m))


"""

1010 - too low
"""