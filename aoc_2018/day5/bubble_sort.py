arr = [5,3,8,7,2]

# def bubble_sort(arr):
#     swap = True

#     while swap:
#         swap = False
#         for i in range(len(arr) - 1):
#             if arr[i] > arr[i + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]
#                 swap = True
    
#     return arr

def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        swap = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True

        if not swap:
            break

    return arr

print(bubble_sort(arr))



