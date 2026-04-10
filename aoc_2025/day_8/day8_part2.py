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
import itertools

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

# def calculate_all_distances(positions):
#     distances = []
#     print('started calculating distances')
#     for box1 in positions:
#         for box2 in positions:
#             distance = calculate_distance(box1, box2)
#             if box1 != box2 and distance not in [dis[0] for dis in distances]:
#                 distances.append([calculate_distance(box1, box2), (box1, box2)])

#     return sorted(distances, key=lambda x: x[0])

def calculate_all_distances(positions):
    distances = []

    for box1, box2 in itertools.combinations(positions, 2):
        distance = calculate_distance(box1, box2)
        distances.append([distance, (box1, box2)])

    return sorted(distances, key=lambda x: x[0])

def calculate_extension_cord_length(coord_pair):
    box1, box2 = coord_pair

    x1 = int(box1.split(',')[0])
    x2 = int(box2.split(',')[0])

    return x1 * x2

# print(calculate_extension_cord_length(['216,146,977', '117,168,530']))

def calculate_circuit_size(distances, num_boxes):
    circuits = []
    print('started calculating circuit')
    for distance, coord_pair in distances:
        # coord_pair = distances[i][1]
        box1, box2 = coord_pair

        index_box1 = next(
            (i for i, circuit in enumerate(circuits) if box1 in circuit),
            -1
            )
        index_box2 = next(
            (i for i, circuit in enumerate(circuits) if box2 in circuit),
            -1
            )
        
        if index_box1 != -1 and index_box1 == index_box2:
            pass
        elif index_box1 != -1 and index_box2 == -1:
            if box2 not in circuits[index_box1]:
                circuits[index_box1].append(box2)
        elif index_box2 != -1 and index_box1 == -1:
            if box1 not in circuits[index_box2]:
                circuits[index_box2].append(box1)
        elif index_box1 == -1 and index_box1 == -1:
            circuits.append([box1, box2])
        elif index_box1 != -1 and index_box2 != -1 and index_box1 != index_box2:
            
            # Determine which index is higher and which is lower
            # L_idx will be the surviving circuit, H_idx will be the deleted circuit
            L_idx = min(index_box1, index_box2)
            H_idx = max(index_box1, index_box2)
            
            # 1. Merge the elements from the circuit at H_idx into the circuit at L_idx
            circuits[L_idx].extend(circuits[H_idx])
            
            # 2. Delete the circuit at the higher index first (This is the critical step!)
            del circuits[H_idx]
            
            # 3. Clean up duplicates in the surviving circuit (L_idx)
            circuits[L_idx] = list(set(circuits[L_idx]))
        # print('COORD PAIR:', coord_pair)
        if len(circuits) == 1 and len(circuits[0]) == num_boxes:
            return calculate_extension_cord_length(coord_pair) 
        
    lengths = [len(circuit) for circuit in sorted(circuits, key=len, reverse=True)]
    
    return math.prod(lengths[:3])

    


# positions = parse_input('example.txt')
positions = parse_input('puzzle.txt')
num_boxes = len(positions)
distances = calculate_all_distances(positions)
# print(distances)
# sol = calculate_circuit_size(distances, num_boxes)
sol = calculate_circuit_size(distances, num_boxes)
print(sol)


"""
552 - too low
"""