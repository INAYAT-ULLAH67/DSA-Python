def quick_sort_stack(arr):
    # stack will store tuples of (low, high) indices
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        print("low is", low, "high is", high)

        if low < high:
            # --- Partition logic inline ---
            pivot = arr[low]   # choose first element as pivot
            i = low + 1
            j = high

            while True:
                while i <= j and arr[i] <= pivot:
                    i += 1
                while i <= j and arr[j] >= pivot:
                    j -= 1
                if i <= j:
                    arr[i], arr[j] = arr[j], arr[i]  # swap
                else:
                    break

            # place pivot in correct position
            arr[low], arr[j] = arr[j], arr[low]
            pivot_index = j
            # --- End partition logic ---

            # Push subarrays onto stack
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return arr


# Example usage
arr = [10, 7, 8, 9, 1, 5]
print("Original array:", arr)
sorted_arr = quick_sort_stack(arr)
print("Sorted array:", sorted_arr)
