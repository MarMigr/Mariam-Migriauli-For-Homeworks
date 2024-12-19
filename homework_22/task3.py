class Stack:
    def __init__(self):
        self.items = []

    def push(self, element):

        self.items.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s.peek())   
print(s.pop())    
print(s.size())  
print(s.is_empty())
s.pop()
s.pop()
print(s.is_empty()) 
