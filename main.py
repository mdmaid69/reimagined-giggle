import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())