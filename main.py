import math
def calculate_hyperbolic_arc_tangent(x):
        return math.atanh(x)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)