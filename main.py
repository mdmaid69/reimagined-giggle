import math
def calculate_logarithm(base, x):
        return math.log(x, base)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())