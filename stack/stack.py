class MyStack:
    def __init__(self):
        self.elements=[]
    def isEmpty(self):
        return len(self.elements)==0
    def push(self,value):
        self.elements.append(value)
    def _pop(self):
        assert not self.isEmpty(),'stack is empty'
        x=self.elements.pop()
        return x
    def display(self):
        for element in self.elements:
            print(element, end=" -> ")
        print("None")

stk=MyStack()
stk.push(20)
stk.push(40)
stk.push(70)
mynums=[30,40,50,70,80,90,100,110,140]
for num in mynums:
    stk.push(num)
stk.display()