import json

class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

class Department:
    def __init__(self, name, description, employees):
        self.name = name
        self.description = description
        self.employees = employees

    def average_salary(self):
        if not self.employees:
            return 0
        return sum(emp.salary for emp in self.employees) / len(self.employees)

    def max_salary(self):
        if not self.employees:
            return 0
        return max(emp.salary for emp in self.employees)

    def min_salary(self):
        if not self.employees:
            return 0
        return min(emp.salary for emp in self.employees)

    def positions_count(self):
        positions = {}
        for emp in self.employees:
            positions[emp.position] = positions.get(emp.position, 0) + 1
        return positions

def load_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file {file_path} is not a valid JSON file.")
        return None

def main():
    file_path = "deps.json"  
    data = load_data(file_path)
    
    if not data:
        return

    departments = []
    for dep_key, dep_info in data.items():
        employees = [
            Employee(emp["name"], emp["position"], float(emp["salary"]))
            for emp in dep_info["employees"]
        ]
        department = Department(dep_info["name"], dep_info["description"], employees)
        departments.append(department)

    for dep in departments:
        print(f"Department: {dep.name}")
        print(f"Description: {dep.description}")
        print(f"Average Salary: {dep.average_salary():.2f}")
        print(f"Max Salary: {dep.max_salary():.2f}")
        print(f"Min Salary: {dep.min_salary():.2f}")
        print(f"Positions Count: {dep.positions_count()}")
        print()


if __name__ == "__main__":
    main()
