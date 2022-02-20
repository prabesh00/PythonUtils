import logging

logging.basicConfig(filename='alog2.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        logging.info(f'Created Employee {self.first} {self.last}')

    @property
    def email(self):
        return f'{self.first}.{self.last}@Employee.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'


if __name__ == '__main__':
    emp_1 = Employee('Clark', 'Kent')
    emp_2 = Employee('Aurther', 'Curry')
    emp_3 = Employee('Barry', 'Allen')
