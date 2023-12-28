import getpass
def get_username():
        return getpass.getuser()
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))