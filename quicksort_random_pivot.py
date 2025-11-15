import random
from stackLS import Stack
def quicksort_random_pivot(arr):
    """
    Quicksort with random pivot selection
    """
    if len(arr) <= 1:
        return arr
    
    stack = Stack()
    stack.push((0, len(arr)-1))
    
    while not stack.isEmpty():
        low, high = stack.pop()
        
        if low >= high:
            continue

        # STEP 1: Generate random pivot index between low and high (inclusive)
        random_index = random.randint(low, high)
        
        # STEP 2: Swap random pivot element to first position
        arr[low], arr[random_index] = arr[random_index], arr[low]
        pivot = arr[low]
        
        # STEP 3: Partition the array around the pivot
        loc = low
        left = low
        right = high
        
        while left < right:
            # Move right pointer leftwards to find element < pivot
            while left < right and arr[right] >= pivot:
                right -= 1
            if left < right:
                arr[loc] = arr[right]
                loc = right
            
            # Move left pointer rightwards to find element > pivot
            while left < right and arr[left] <= pivot:
                left += 1
            if left < right:
                arr[loc] = arr[left]
                loc = left
        
        # Place pivot in its final position
        arr[loc] = pivot
        
        # STEP 4: Push subarrays to stack
        stack.push((low, loc - 1))
        stack.push((loc + 1, high))
    
    return arr