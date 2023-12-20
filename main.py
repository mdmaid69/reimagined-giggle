import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)