import math
def calculate_permutations(n, k):
        return math.perm(n, k)
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())