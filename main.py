import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import math
def calculate_modulus(x, y):
        return math.fmod(x, y)