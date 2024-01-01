import math
def calculate_combinations(n, k):
        return math.comb(n, k)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())