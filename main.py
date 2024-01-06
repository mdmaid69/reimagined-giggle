import datetime
def get_current_datetime():
        return datetime.datetime.now()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)