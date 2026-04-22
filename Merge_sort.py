# Merge sort implementation

def merge_sort(arr: list) -> list:
    n = len(arr)

    if n <= 1:
        return arr

    mid = n // 2

    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left: list, right: list) -> list:
    result = []
    i = 0
    j = 0

    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


test_arr = [33, 14, 55, 1, 3]
sorted_arr = merge_sort(test_arr.copy())
print(f"Unsorted arr: {test_arr}")
print(f"Sorted arr: {sorted_arr}")