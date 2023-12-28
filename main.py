import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import math
def calculate_euclidean_distance(p, q):
        return math.dist(p, q)