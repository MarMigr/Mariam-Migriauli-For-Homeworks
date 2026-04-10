class Queue:
    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise IndexError("pop from an empty queue")
        return self.items.pop(0)

q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
print(q.pop()) 
