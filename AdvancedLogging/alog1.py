import logging
from alog2 import Employee

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')
file_handler = logging.FileHandler('alog1.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


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
logger.debug(f'Added {a} and {b} to get {addition}')

diff = subtract(a, b)
logger.debug(f'Subtracted {b} from {a} to get {diff}')

multiple = multiply(a, b)
logger.debug(f'Multiplied {a} and {b} to get {multiple}')

division = divide(a, b)
logger.debug(f'Divided {a} by {b} to get {division}')
