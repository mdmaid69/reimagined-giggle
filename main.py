import tensorflow as tf
print(tf.__version__)
import math
def calculate_cone_volume(radius, height):
        return 1/3 * math.pi * radius**2 * height