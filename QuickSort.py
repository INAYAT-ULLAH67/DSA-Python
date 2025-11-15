def quicksort(arr):
    # Create an empty stack
    stack = []
    
    # Push the initial sequence (start and end indices)
    stack.append((0, len(arr) - 1))
    
    while stack:
        # Step 1: Pop sequence from stack
        low, high = stack.pop()

        if low >= high:
            continue

        # Step 2: Select first element as pivot
        pivot = arr[low]
        loc = low
        left = low
        right = high

        while left < right:
            # Step 3: Scan from right to left for smaller than pivot
            #this will stop when we encounter smaller value than pivot!
            while left < right and arr[right] >= pivot:
                right -= 1
            if left < right:
                arr[loc] = arr[right]
                loc = right

            # Step 4: Scan from left to right for larger than pivot
            #this loop will stop when it encounter larger value 
            while left < right and arr[left] <= pivot:
                left += 1
            if left < right:
                arr[loc] = arr[left]
                loc = left

        # Place pivot at correct location
        arr[loc] = pivot

        # Step 6: Push left and right sequences onto stack
        # L = left part, G = right part
        stack.append((low, loc - 1))
        stack.append((loc + 1, high))

    return arr




# Example usage
arr = [50, 30, 70, 20, 90, 40]
print("Original array:", arr)
sorted_arr = quicksort(arr)
print("Sorted array:", sorted_arr)
