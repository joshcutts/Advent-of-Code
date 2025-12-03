'''

- initailize invalid id sum at 0
- get all id's in an array
- loop through all ids
    - if id is invalid, add to invalid id sum
- return invalid id sum

check for invalid id (is_invalid)
invalid id is made only of some sequence of digits repeated twice.
- pointer at start of string (left)
- pointer at halfway through string (right)
- while right is less than length of string
    - return false if the digits are different
- return true (the digits were same on left and right)



'''

def parse_input(filename):
    with open (filename, "r") as f:
        str_ids = f.read().split(',')
    
    return [id_range.split('-') for id_range in str_ids]

'''
result = []
for id in str_ids:
    for i in id.split('-'):
        result.append(i)

'''

def is_invalid(id):
    length = len(id)
    if length % 2 == 1:
        return False
    
    left = 0
    right = int(length / 2)

    while right < length:
        if (id[left] != id[right]):
            return False
        
        left += 1
        right += 1

    return True

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


# print(is_invalid('11')) # True
# print(is_invalid('998')) # False
# print(is_invalid('222222')) # True


# id_ranges = parse_input('example.txt')
id_ranges = parse_input('part1_input.txt')

print(identify_and_sum_invalid_ids(id_ranges))