import tensorflow as tf
print(tf.__version__)
import math
def calculate_cylinder_volume(radius, height):
        return math.pi * radius**2 * height