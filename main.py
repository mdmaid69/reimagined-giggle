import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))