class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return f'{self.first}.{self.last}@Employee.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f'Employee {self.first} {self.last}, {self.pay}'


if __name__ == '__main__':
    emp_1 = Employee('Clark', 'Kent')
    emp_2 = Employee('Aurther', 'Curry')
    emp_3 = Employee('Barry', 'Allen')
