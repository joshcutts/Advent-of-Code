"""
Docstring for aoc_2025.day_8.day8_part1

162,817,812 X
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689 X

(box1, box2): dist
"""
import math
def parse_input(filename):
    with open(filename, "r") as f:
        positions = f.read().splitlines()

    return dict([[coord, True] for coord in positions])


def calculate_distance(coord_one, coord_two):
    coord_one_list = [int(n) for n in coord_one.split(',')]
    coord_two_list = [int(n) for n in coord_two.split(',')]
    sum = 0

    for i in range(3):
        sum += (coord_one_list[i] - coord_two_list[i]) ** 2

    return math.sqrt(sum)

def calculate_all_distances(positions):
    distances = []

    for box1 in positions:
        for box2 in positions:
            distance = calculate_distance(box1, box2)
            if box1 != box2 and distance not in [dis[0] for dis in distances]:
                distances.append([calculate_distance(box1, box2), (box1, box2)])

    return sorted(distances, key=lambda x: x[0])



def calculate_circuit_size(distances, pair_num):
    circuits = []

    for i in range(pair_num):
        coord_pair = distances[i][1]
        box1, box2 = coord_pair

        index_box1 = next(
            (i for i, circuit in enumerate(circuits) if box1 in circuit),
            -1
            )
        index_box2 = next(
            (i for i, circuit in enumerate(circuits) if box2 in circuit),
            -1
            )
        
        if index_box1 != -1:
            circuits[index_box1].append(box2)
        elif index_box2 != -1:
            circuits[index_box2].append(box1)
        else:
            circuits.append([box1, box2])
        
    lengths = [len(circuit) for circuit in sorted(circuits, key=len, reverse=True)]
    return math.prod(lengths[:2])

    


positions = parse_input('example.txt')
# positions = parse_input('puzzle.txt')
distances = calculate_all_distances(positions)
print(distances)
# sol = calculate_circuit_size(distances, 10)
sol = calculate_circuit_size(distances, 1000)
print(sol)

# print(calculate_distance('162,817,812', '425,690,689')) # 316.902
# print(calculate_circuit_size(positions))

# d = {(1, 2): 111, (2, 3): 222, (3, 4): 333}
# for element in d:
#     if 2 in element:
#         del d[element]
# print(d)

