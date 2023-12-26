import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())