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





manifold = parse_input('example.txt')
# manifold = parse_input('puzzle.txt')
# print(find_s(manifold))
start = find_s(manifold)
for m in manifold:
    print("".join(m))


