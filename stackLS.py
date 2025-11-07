from node import Node

class Stack:
    def __init__(self):
        self.tos = None   # top of stack

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
        return self.tos.data   # return value

    def display(self):
        current = self.tos
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage
stk = Stack()
stk.push(20)
stk.push(40)
stk.push(70)

mynums = [30, 40, 50, 70, 80, 90, 100, 110, 140]
for num in mynums:
    stk.push(num)

stk.display()
print("Top element (peek):", stk.peek())
print("Popped element:", stk.pop())
stk.display()
