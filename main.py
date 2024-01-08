import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())