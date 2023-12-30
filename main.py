import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)