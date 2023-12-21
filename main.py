import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())