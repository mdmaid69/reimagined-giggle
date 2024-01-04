import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import platform
def get_os_info():
        return platform.uname()