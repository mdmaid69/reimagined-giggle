import math
def calculate_least_common_multiple(a, b):
        return abs(a*b) // math.gcd(a, b)
import tensorflow as tf
print(tf.__version__)