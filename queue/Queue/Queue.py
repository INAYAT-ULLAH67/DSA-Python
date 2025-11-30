from qnode import Node

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return temp.data

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data
    def display(self):
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
# Queue.py --- IGNORE ---     
# End of Queue.py --- IGNORE ---
obj=Queue()
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.display()
print("Dequeued:", obj.dequeue())
obj.display()
print("Front element is:", obj.peek())
obj.enqueue(40)
obj.display()
obj.enqueue(50)
obj.display()