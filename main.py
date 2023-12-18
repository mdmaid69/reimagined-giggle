import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)