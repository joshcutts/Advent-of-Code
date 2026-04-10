"""


"""

"""
template

left = 0
right = len(arr) - 1

while left <= right
    mid = math.floor((left + right) / 2) 

    if array[mid] == target
        # optional early return
    elif # comparison
        left = mid + 1
    else
        right = mid - 1

"""

import math

def find_zero_position(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = math.floor((left + right) / 2)

        if arr[mid] == 0:
            return mid
        elif arr[mid] > 0:
            right = mid - 1
        else:
            left = mid + 1

    return left

print(find_zero_position([-7,-5,-3,0,2]))
print(find_zero_position([-7,-5,-3,2,3]))
print(find_zero_position([3,5,7,9,11]))