"""
Docstring for aoc_2025.day_5.day5_part1


"""

def parse_input(filename):
    with open(filename, "r") as f:
        ranges, ingredients = f.read().split('\n\n')

    # formatted_ranges = [[r.split('-')] for r in ranges.splitlines()]
    formatted_ranges = [
        [int(n) for n in range_line.split('-')]
        for range_line in ranges.splitlines()
    ]
    formatted_ingredients = [int(ingredient) for ingredient in ingredients.splitlines()]

    return formatted_ranges, formatted_ingredients

def combine_ranges(ranges):
    ranges.sort(key=lambda x: x[0])
    final_ranges = [ranges[0]]

    for r in ranges:
        found_overlap = False
        start, end = r

        for fi, final_range in enumerate(final_ranges):
            final_start, final_end = final_range
            if start >= final_start and start <= final_end and end > final_end:
                final_ranges[fi][1] = end
                found_overlap = True
            elif end >= final_start and end <= final_end and start < final_start:
                final_ranges[fi][0] = start
                found_overlap = True
            elif start >= final_start and end <= final_end:
                found_overlap = True
                pass
            
        if not found_overlap:
            final_ranges.append(r)
        

    return final_ranges

def sum_fresh_ingredients(combined_ranges):
    fresh_ingredients = 0

    for r in combined_ranges:
        start, end = r
        fresh_ingredients += (end - start + 1)

    return fresh_ingredients

# ranges, igredients = parse_input('example.txt')
ranges, igredients = parse_input('puzzle.txt')


# print(combine_ranges(ranges))
combined_ranges = combine_ranges(ranges)
print(sum_fresh_ingredients(combined_ranges))