import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('alog2.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info(f'Created Employee {self.first}.{self.last}@Employee.com')

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
