class Insert:
    def __init__(self):
        self.elements = []

    def insert(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def member(self, element):
        return element in self.elements

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            raise ValueError("Not found")

    def __str__(self):
        return str(sorted(self.elements))

Insert = Insert()
Insert.insert(3)
Insert.insert(1)
Insert.insert(3)  
print(Insert)   
print(Insert.member(3))  
print(Insert.member(2))  
Insert.remove(1)
print(Insert) 
