import collections
def create_stack():
        return collections.deque()
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)