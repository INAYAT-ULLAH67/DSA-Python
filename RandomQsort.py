import random
from node import Node

class Stack:
    def __init__(self):
        self.tos = None  # top of stack
    
    def isEmpty(self):
        return self.tos is None
    
    def push(self, value):
        x = Node(value)
        x.next = self.tos
        self.tos = x
    
    def pop(self):
        assert not self.isEmpty(), "Stack is empty"
        x = self.tos.data
        self.tos = self.tos.next
        return x
    
    def peek(self):
        assert not self.isEmpty(), "Stack is empty"
        return self.tos.data
    
    def display(self):
        current = self.tos
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def quicksort_median_of_three(arr):
    stack = Stack()
    stack.push((0, len(arr)-1))
    
    while not stack.isEmpty():
        low, high = stack.pop()
        
        if low >= high:
            continue

        # MEDIAN-OF-THREE PIVOT SELECTION
        # Generate three random indices between low and high (inclusive)
        x = random.randint(low, high)
        y = random.randint(low, high)
        z = random.randint(low, high)
        
        # Find the median value among arr[x], arr[y], arr[z]
        three_values = [(arr[x], x), (arr[y], y), (arr[z], z)]
        three_values.sort(key=lambda pair: pair[0])  # Sort by value
        
        # The median is the middle element after sorting
        median_value, median_index = three_values[1]
        
        # Set pivot to the median value and swap median element to first position
        pivot = median_value
        arr[low], arr[median_index] = arr[median_index], arr[low]
        
        # Rest of partitioning algorithm remains the same
        loc = low
        left = low
        right = high
        
        while left < right:
            # Scan from right to left for element smaller than pivot
            while left < right and arr[right] >= pivot:
                right -= 1
            if left < right:
                arr[loc] = arr[right]
                loc = right
            
            # Scan from left to right for element larger than pivot
            while left < right and arr[left] <= pivot:
                left += 1
            if left < right:
                arr[loc] = arr[left]
                loc = left
        
        # Place pivot at correct location
        arr[loc] = pivot
        
        # Push subarrays to stack
        stack.push((low, loc - 1))
        stack.push((loc + 1, high))
    
    return arr

