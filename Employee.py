class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name} is doing regular work.")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)

        self.team_size = team_size

    def work(self):
        super().work()
        print(f"{self.name} is managing {self.team_size} people.")

manager = Manager("Ana", 80000, 5)

manager.work()

print(f"Name: {manager.name}")
print(f"Salary: {manager.salary}")
print(f"Team Size: {manager.team_size}")

print(f"Is manager an Employee? {isinstance(manager, Employee)}")
print(f"Is manager a Manager? {isinstance(manager, Manager)}")