"""

"""

# def searchMatrix(matrix, target):
#     outer_left = 0
#     outer_right = len(matrix) - 1

#     while outer_left <= outer_right:
#         outer_mid = (outer_left + outer_right) // 2
#         arr = matrix[outer_mid]
#         arr_min = arr[0]
#         arr_max = arr[-1]

#         if target >= arr_min and target <= arr_max:
#             left = 0
#             right = len(arr) - 1

#             while left <= right:
#                 mid = (left + right) // 2
#                 if arr[mid] == target:
#                     return True
#                 elif arr[mid] > target:
#                     right = mid - 1
#                 else:
#                     left = mid + 1

#             return False

#         elif target < arr_min:
#             outer_right = outer_mid - 1
#         else:
#             outer_left = outer_mid + 1

#     return False

# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
