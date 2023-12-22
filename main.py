import tensorflow as tf
print(tf.__version__)
import math
def calculate_polar_to_cartesian_coordinates(r, theta):
        return math.polar((r, theta))