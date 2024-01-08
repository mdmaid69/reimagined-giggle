import tensorflow as tf
print(tf.__version__)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)