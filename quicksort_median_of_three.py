def quicksort(arr):
    def sort(left, right):
        if left >= right:
            return

        # ---- Median of Three ----
        mid = (left + right) // 2
        if arr[left] > arr[mid]:
            arr[left], arr[mid] = arr[mid], arr[left]
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
        if arr[mid] > arr[right]:
            arr[mid], arr[right] = arr[right], arr[mid]
        # Now arr[mid] is the median — use it as pivot
        pivot = arr[mid]

        loc = mid
        l = left
        r = right

        while l < r:
            # Scan from right to left for smaller than pivot
            while l < r and arr[r] >= pivot:
                r -= 1
            if l < r:
                arr[loc] = arr[r]
                loc = r

            # Scan from left to right for larger than pivot
            while l < r and arr[l] <= pivot:
                l += 1
            if l < r:
                arr[loc] = arr[l]
                loc = l

        arr[loc] = pivot  # Place pivot in correct location

        # ---- Recursive Calls ----
        sort(left, loc - 1)
        sort(loc + 1, right)

    sort(0, len(arr) - 1)
    return arr


# Example usage
arr = [60, 20, 80, 40, 10, 90, 30]
print("Before sorting:", arr)
print("After sorting:", quicksort(arr))