def quicksort_middle_pivot(arr):
    stack = []
    stack.append((0, len(arr) - 1))
    
    while stack:
        low, high = stack.pop()
        
        if low >= high:
            continue

        # MODIFICATION: Choose middle element and swap with first
        mid = (low + high) // 2
        pivot = arr[mid]
        # Swap middle element with first element
        arr[low], arr[mid] = arr[mid], arr[low]  # ← SWAPPING OCCURS HERE
        
        # Now the pivot is at arr[low], so rest of algorithm works the same
        loc = low
        left = low
        right = high
        
        while left < right:
            while left < right and arr[right] >= pivot:
                right -= 1
            if left < right:
                arr[loc] = arr[right]
                loc = right
            
            while left < right and arr[left] <= pivot:
                left += 1
            if left < right:
                arr[loc] = arr[left]
                loc = left
        
        arr[loc] = pivot
        
        stack.append((low, loc - 1))
        stack.append((loc + 1, high))
    
    return arr