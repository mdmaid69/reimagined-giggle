import tensorflow as tf
print(tf.__version__)
import math
def calculate_sign(x):
        return math.copysign(1, x)