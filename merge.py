def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    # Divide the array
    left_half = mergeSort(arr[:mid])
    right_half = mergeSort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare elements of both halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add remaining elements
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
print("Sorted:", mergeSort(arr))
