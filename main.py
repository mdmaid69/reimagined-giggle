import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())