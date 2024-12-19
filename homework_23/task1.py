class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name):
        if not _name:
            raise ValueError("Name cannot be empty.")
        self._name = _name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, _age):
        if not isinstance(_age, int) or _age <= 0:
            raise ValueError("Age must be a positive integer.")
        self._age = _age

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"


person1 = Person("Mariam", 25)
person2 = Person("Nini", 27)
person3 = Person("Elene", 42)

print(person1.get_info())
print(person2.get_info())
print(person3.get_info())

person1.name = "Mariam"
person1.age = 26
print(person1.get_info())
