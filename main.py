import math
def calculate_sign(x):
        return math.copysign(1, x)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())