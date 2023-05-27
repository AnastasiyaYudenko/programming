class Employee:
    def __init__(self, n, ln):
        self.name = n
        self.lastname = ln


class Headmaster(Employee):
    def __init__(self, n, ln, s):
        super().__init__(n, ln)
        self.salary = s * 3

    def get_info(self):
        print(self.name, self.lastname, self.salary)

    def set_salary(self, ns):
        self.salary = ns


class Manager(Employee):
    def __init__(self, n, ln, s, h):
        super().__init__(n, ln)
        self.salary = s * 2
        self.hours = h

    def get_info(self):
        print(self.name, self.lastname, self.salary, self.hours)

    def set_hours(self, h):
        self.hours = h


class Trainee(Employee):
    def __init__(self, n, ln, h):
        super().__init__(n, ln)
        self.hour = h - 2

    def get_info(self):
        print(self.name, self.lastname, self.hour)

    def set_mark(self, m):
        self.mark = m


t = Trainee('Tom', 'Gordon', 8)
t.get_info()
n = Manager('Natasha', 'Denisova', 30, 8)
n.get_info()
e = Headmaster('Eseniya', 'Kirova', 40)
e.get_info()