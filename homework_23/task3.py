class Student:
    def __init__(self, name):
        self._name = name
        self._scores = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        self._name = name

    @property
    def scores(self):
        return self._scores

    @scores.setter
    def scores(self, scores):
        if not all(0 <= score <= 100 for score in scores):
            raise ValueError("All scores must be between 0 and 100.")
        self._scores = scores

    def add_score(self, score):
        if 0 <= score <= 100:
            self.scores.append(score)
        else:
            print("არასწორი ქულა,ქულა უნდა იყოს 0 და 100 ის ინტერვალში")

    def get_average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def get_scores(self):
        return self.scores



students = [Student("მარიამი"), Student("ნინი"), Student("ელენე")]

students[0].add_score(95)
students[0].add_score(88)
students[1].add_score(5)
students[1].add_score(26)
students[1].add_score(90)
students[2].add_score(63)
students[2].add_score(1)
students[2].add_score(39)

for student in students:
    print(f"{student.name} - სულ ქულები: {student.get_scores()}, საშუალო ქულა: {student.get_average():.2f}")

new_student = Student("დათო")
new_student.add_score(110)
new_student.add_score(90)
print(f"{new_student.name}  - სულ ქულები: {new_student.get_scores()}, საშუალო ქულა: {new_student.get_average():.2f}")
