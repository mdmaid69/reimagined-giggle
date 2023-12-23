import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)