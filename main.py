import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import time
def get_current_time():
        return time.ctime()