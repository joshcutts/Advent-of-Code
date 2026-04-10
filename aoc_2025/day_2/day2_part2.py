"""


part 1 examples

11-22 has two invalid IDs, 11 and 22.
95-115 has one invalid ID, 99.
998-1012 has one invalid ID, 1010.
1188511880-1188511890 has one invalid ID, 1188511885.
222220-222224 has one invalid ID, 222222.
1698522-1698528 contains no invalid IDs.
446443-446449 has one invalid ID, 446446.
38593856-38593862 has one invalid ID, 38593859.
The rest of the ranges contain no invalid IDs:
565653-565659
824824821-824824827
2121212118-2121212124


part 2 examples

11-22 still has two invalid IDs, 11 and 22.
95-115 now has two invalid IDs, 99 and 111.
998-1012 now has two invalid IDs, 999 and 1010.
1188511880-1188511890 still has one invalid ID, 1188511885.
222220-222224 still has one invalid ID, 222222.
1698522-1698528 still contains no invalid IDs.
446443-446449 still has one invalid ID, 446446.
38593856-38593862 still has one invalid ID, 38593859.
565653-565659 now has one invalid ID, 565656.
824824821-824824827 now has one invalid ID, 824824824.
2121212118-2121212124 now has one invalid ID, 2121212121.
"""
import math

def parse_input(filename):
    with open (filename, "r") as f:
        str_ids = f.read().split(',')
    
    return [id_range.split('-') for id_range in str_ids]


def is_invalid(id):
    for i in range(1, len(id)):
        
        repeat_test = id[0:i]
        
        chunks = []
        for j in range(0, len(id), i):
            current_chunk = id[j:j+i]
            chunks.append(current_chunk)
            
        
        invalid = all(chunk == repeat_test for chunk in chunks)
        if invalid == True:
            return True
    return False

def identify_and_sum_invalid_ids(id_ranges):
    invalid_id_sum = 0

    for id_range in id_ranges:
        start, end = [int(id) for id in id_range]

        while (start <= end):
            if is_invalid(str(start)):
                invalid_id_sum += start
                start += 1
            
            start += 1
    
    return invalid_id_sum



# print(is_invalid('824824824')) # True
# print(is_invalid('2121212121')) # True
# print(is_invalid('2121212122')) # False
# print(is_invalid('11')) # True


# id_ranges = parse_input('example.txt')
id_ranges = parse_input('part1_input.txt')

print(identify_and_sum_invalid_ids(id_ranges))