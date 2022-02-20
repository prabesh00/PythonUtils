import logging

logging.basicConfig(filename='test1.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


a = 16
b = 8

addition = add(a, b)
logging.debug(f'Added {a} and {b} to get {addition}')

diff = subtract(a, b)
logging.debug(f'Subtracted {b} from {a} to get {diff}')

multiple = multiply(a, b)
logging.debug(f'Multiplied {a} and {b} to get {multiple}')

division = divide(a, b)
logging.debug(f'Divided {a} by {b} to get {division}')
