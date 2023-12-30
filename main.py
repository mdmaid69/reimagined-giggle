import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)