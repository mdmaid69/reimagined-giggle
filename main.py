import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
import time
def get_current_time():
        return time.ctime()