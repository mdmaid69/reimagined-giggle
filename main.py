import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)